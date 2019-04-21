from django.contrib import admin
from .models import Food, FoodCategory

# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(Food)
