from django.contrib import admin

from . models import *

admin.site.register(CheckoutRequest)
admin.site.register(Vehicle)


# @admin.register(Vehicle)
# class VehicleAdmin(admin.ModelAdmin):
#     list_display = ('id')
#     # list_filter = ('verified_by_superuser', )
#     search_fields = ('id',)
#     readonly_fields = ('id',)
#     actions = ['verify_checkout']

#     # def checkout_pending(self, obj):
#     #     return not obj.verified_by_superuser
#     # checkout_pending.boolean = True
#     # checkout_pending.short_description = "Checkout Pending"

#     # def get_queryset(self, request):
#     #     queryset = super().get_queryset(request)
#     #     return queryset.filter(verified_by_superuser=False)

#     def verify_checkout(self, request, queryset):
#         for vehicle in queryset:
#             CheckoutRequest.is_verified = True
#             vehicle.save()
#     verify_checkout.short_description = "Verify selected vehicles for checkout"