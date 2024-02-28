from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import VehicleForm,VendorForm,ProductForm
from .models import Vehicle, Vendor, Product,CheckoutRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login/')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        vendor_form = VendorForm(request.POST)
        if vendor_form.is_valid():
            vendor_form.save()
            return redirect('select_product')
    else:
        vendor_form = VendorForm()
    return render(request, 'dashboard.html', {'form': vendor_form})

@login_required
def select_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('enter_vehicle_data')
    else:
        product_form = ProductForm()
    return render(request, 'select_product.html', {'form': product_form})

@login_required
def enter_vehicle_data(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('success')  
    else:
        form = VehicleForm()
    return render(request, 'vehicle.html', {'form': form})


@login_required
def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

@login_required
def userlogout(request):
    logout(request)
    return redirect("login")

@login_required
def success(request):
    fm=Vehicle.objects.all()
    return render(request, 'success.html',{"fm":fm})


# @user_passes_test(lambda u: u.is_superuser)
# @login_required
# def vehicle_checkout(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
#     vehicle.checked_out = True
#     vehicle.verified_by_superuser = True
#     vehicle.save()
#     vehicle.delete()
#     return render(request, 'vehicle_checkout_success.html',{'vehicle': vehicle})

@login_required
def vehicle_checkout(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    checkout_request = CheckoutRequest.objects.create(user=request.user, vehicle=vehicle)
    # vehicle.delete()

    
    return render(request, 'vehicle_checkout_success.html', {'vehicle': checkout_request})

@login_required
def search_by_po_number(request):
    if request.method == 'POST':
        po_number = request.POST.get('po_number', None)
        if po_number:
            vehicles = Vehicle.objects.filter(po_number=po_number)
            return render(request, 'search_results.html', {'products': vehicles, 'vehicles': vehicles})
        else:
            return HttpResponse("Please provide a PO number for the search.")
    else:
        return render(request, 'search_form.html')
