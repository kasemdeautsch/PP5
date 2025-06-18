from django.contrib import admin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number')
#admin.site.register(UserProfile)