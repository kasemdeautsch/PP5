from django import forms
from .models import Product, Brand
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    image = forms.ImageField(label='Image', widget=CustomClearableFileInput,
                             required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        other_names = [(c.id, c.get_other_name()) for c in brands]
        self.fields['brand'].choices = other_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
