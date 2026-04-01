# from django.contrib import admin
# from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

# Inline class to show CarModels inside CarMake admin page
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # Number of empty forms to display

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country')
    inlines = [CarModelInline]

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name', 'car_make__name')

# Register models with admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)


# Registering models with their respective admins

# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
