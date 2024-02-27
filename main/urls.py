from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('', views.user_signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/',views.userlogout, name='logout'),
    path('product/',views.select_product, name='select_product'),
    path('vehicle/',views.enter_vehicle_data, name='enter_vehicle_data'),
    path('success/',views.success, name='success'),
    path('vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:vehicle_id>/checkout/', views.vehicle_checkout, name='vehicle_checkout'),
    path('search/',views.search_by_po_number, name='search_by_po_number')
]
