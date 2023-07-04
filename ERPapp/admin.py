from django.contrib import admin
from .models import Employee,Type,Product,Category,Client,Sale,DetSale
# Register your models here.
admin.site.register(Employee)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(DetSale)