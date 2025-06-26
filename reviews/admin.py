from django.contrib import admin
from .models import Reviews

# Register your models here.


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'rating', 'review', 'updated_on')
    
