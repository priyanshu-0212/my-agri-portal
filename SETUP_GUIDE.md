# Fair Trade Agri Portal - Quick Setup Guide

## Quick Start

### 1. Start the Server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

### 2. Create a Superuser (Optional)
To access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit: **http://127.0.0.1:8000/admin/**

### 3. User Roles

#### Register as a Farmer:
1. Click "Register" on the home page
2. Select "Farmer" as your role
3. Fill in your details
4. After registration, login
5. You'll see the Farmer Dashboard
6. Click "Add New Product" to list your crops

#### Register as a Buyer:
1. Click "Register" on the home page
2. Select "Buyer" as your role
3. Fill in your details
4. After registration, login
5. You'll see a "Browse Crops" option
6. Browse available products and send inquiries

## Features Overview

### For Farmers:
- ✅ Add/Edit/Delete crop listings
- ✅ View inquiries from buyers
- ✅ Manage inquiry status
- ✅ Upload product images
- ✅ Set prices and quantities

### For Buyers:
- ✅ Browse all available crops
- ✅ Search by name or description
- ✅ Filter by price (low to high / high to low)
- ✅ Send inquiries to farmers
- ✅ View sent inquiries

### Market Rates:
- ✅ View current market prices for various crops
- ✅ Compare your prices with market rates
- Admin can update rates via `/admin/`

## Testing the Application

### Create Test Users:

**Farmer Test Account:**
- Username: `farmer1`
- Email: `farmer@test.com`
- Role: Farmer
- Password: `farmer123`

**Buyer Test Account:**
- Username: `buyer1`
- Email: `buyer@test.com`
- Role: Buyer
- Password: `buyer123`

### Test Workflow:

1. **Register as Farmer:**
   - Register with farmer role
   - Add 2-3 products with images
   - View the farmer dashboard

2. **Register as Buyer:**
   - Register with buyer role
   - Browse crops from farmer
   - Send an inquiry on a product
   - View your sent inquiries

3. **Check Inquiries:**
   - Login as farmer
   - Go to "Inquiries" in navbar
   - View buyer's inquiry
   - Update inquiry status (responded/closed)

## Sample Data

Market rates are already populated with:
- Wheat, Rice, Tomato, Potato, Onion
- Corn, Cabbage, Carrot, Cauliflower, Spinach

Feel free to add more market rates via the admin panel.

## Common Issues

### Issue: Images not displaying
**Solution:** Make sure the `media` folder exists in the project root

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic` (not needed for development)

### Issue: Permission denied errors
**Solution:** Make sure Python has read/write permissions in the project directory

### Issue: Database errors
**Solution:** Delete `db.sqlite3` and run migrations again:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell < add_sample_market_rates.py
```

## URLs Reference

- Home: `/`
- Register: `/register/`
- Login: `/login/`
- Farmer Dashboard: `/farmer/dashboard/`
- Buyer Dashboard: `/buyer/dashboard/`
- Add Product: `/farmer/product/add/`
- Market Rates: `/market-rates/`
- Contact: `/contact/`
- My Inquiries: `/inquiries/`
- Admin Panel: `/admin/`

## Navigation

The application has a responsive navigation bar that adapts to:
- Logged out users: Shows Login/Register options
- Farmers: Shows Farmer Dashboard, Inquiries
- Buyers: Shows Browse Crops, Inquiries

## Tips

1. **Use good quality images** for better product presentation
2. **Update market rates regularly** to reflect current prices
3. **Respond to inquiries promptly** for better user engagement
4. **Use search and filters** when browsing products
5. **Contact page** is available for support

## Next Steps

Consider adding:
- Email notifications for inquiries
- Payment gateway integration
- Product reviews and ratings
- Advanced search with more filters
- Farmer/Buyer profiles
- Order management system

Enjoy using the Fair Trade Agri Portal!
