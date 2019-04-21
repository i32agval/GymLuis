from django.contrib import admin
from .models import (
    UserProfile, WeightData, Machine, Exercise, UserImages, Relationship)

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(WeightData)
admin.site.register(Machine)
admin.site.register(Exercise)
admin.site.register(UserImages)
admin.site.register(Relationship)
