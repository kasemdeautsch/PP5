from django.contrib import admin
from .models import Faqs

# Register your models here.


@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    
    list_display = ('question',)
    
    class Meta:
        ordering = ['question']


