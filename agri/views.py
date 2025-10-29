from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import User, Product, Inquiry, MarketRate
from .forms import UserRegistrationForm, ProductForm, InquiryForm


def home(request):
    """Home page"""
    # Get latest products for display
    latest_products = Product.objects.filter(is_available=True).order_by('-created_at')[:6]
    
    # Get market rates for home page
    market_rates = MarketRate.objects.all()[:5]
    
    context = {
        'latest_products': latest_products,
        'market_rates': market_rates,
    }
    return render(request, 'agri/home.html', context)


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created successfully for {user.username}! Please login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'agri/register.html', {'form': form})


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def farmer_dashboard(request):
    """Farmer dashboard showing their products"""
    products = Product.objects.filter(farmer=request.user)
    
    context = {
        'products': products,
    }
    return render(request, 'agri/farmer_dashboard.html', context)


@login_required
def buyer_dashboard(request):
    """Buyer dashboard showing all available products"""
    products = Product.objects.filter(is_available=True)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Price filter
    price_filter = request.GET.get('price_filter')
    if price_filter == 'low':
        products = products.order_by('price_per_unit')
    elif price_filter == 'high':
        products = products.order_by('-price_per_unit')
    
    context = {
        'products': products,
        'search_query': search_query,
        'price_filter': price_filter,
    }
    return render(request, 'agri/buyer_dashboard.html', context)


@login_required
def product_add(request):
    """Add new product (Farmer only)"""
    if request.user.role != 'farmer':
        messages.error(request, 'Only farmers can add products.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('farmer_dashboard')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'action': 'Add',
    }
    return render(request, 'agri/product_form.html', context)


@login_required
def product_edit(request, pk):
    """Edit existing product (Owner only)"""
    product = get_object_or_404(Product, pk=pk)
    
    if product.farmer != request.user:
        messages.error(request, 'You can only edit your own products.')
        return redirect('farmer_dashboard')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('farmer_dashboard')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'action': 'Edit',
    }
    return render(request, 'agri/product_form.html', context)


@login_required
def product_delete(request, pk):
    """Delete product (Owner only)"""
    product = get_object_or_404(Product, pk=pk)
    
    if product.farmer != request.user:
        messages.error(request, 'You can only delete your own products.')
        return redirect('farmer_dashboard')
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('farmer_dashboard')
    
    context = {
        'product': product,
    }
    return render(request, 'agri/product_delete.html', context)


def product_detail(request, pk):
    """Product detail view"""
    product = get_object_or_404(Product, pk=pk)
    
    context = {
        'product': product,
    }
    return render(request, 'agri/product_detail.html', context)


@login_required
def send_inquiry(request, pk):
    """Send inquiry for a product (Buyer only)"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.user.role != 'buyer':
        messages.error(request, 'Only buyers can send inquiries.')
        return redirect('product_detail', pk=pk)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.buyer = request.user
            inquiry.product = product
            inquiry.save()
            messages.success(request, 'Inquiry sent successfully!')
            return redirect('product_detail', pk=pk)
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'agri/send_inquiry.html', context)


@login_required
def my_inquiries(request):
    """View inquiries made by buyer or received by farmer"""
    if request.user.role == 'buyer':
        inquiries = Inquiry.objects.filter(buyer=request.user)
    else:  # farmer
        inquiries = Inquiry.objects.filter(product__farmer=request.user)
    
    context = {
        'inquiries': inquiries,
    }
    return render(request, 'agri/my_inquiries.html', context)


@login_required
def update_inquiry_status(request, pk, status):
    """Update inquiry status"""
    inquiry = get_object_or_404(Inquiry, pk=pk)
    
    if request.user != inquiry.product.farmer:
        messages.error(request, 'You can only update status for inquiries on your products.')
        return redirect('my_inquiries')
    
    inquiry.status = status
    inquiry.save()
    messages.success(request, 'Inquiry status updated!')
    return redirect('my_inquiries')


def market_rates(request):
    """Display market rates"""
    rates = MarketRate.objects.all()
    
    context = {
        'rates': rates,
    }
    return render(request, 'agri/market_rates.html', context)


def contact(request):
    """Contact page"""
    return render(request, 'agri/contact.html')