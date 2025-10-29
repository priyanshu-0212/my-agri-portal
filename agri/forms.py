from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product, Inquiry, MarketRate


class UserRegistrationForm(UserCreationForm):
    """Registration form with role selection"""
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    """Form for creating/editing product listings"""
    
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'unit', 'price_per_unit', 'description', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class InquiryForm(forms.ModelForm):
    """Form for sending inquiries to farmers"""
    
    class Meta:
        model = Inquiry
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your inquiry message here...'}),
        }


class MarketRateForm(forms.ModelForm):
    """Form for market rates (admin use)"""
    
    class Meta:
        model = MarketRate
        fields = ['crop_name', 'average_price', 'unit', 'notes']
        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'average_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
