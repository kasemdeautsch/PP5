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
        # for id, name in other_names:
        #     print(f'id: {id}, name: {name}')

        print('other_names: ', other_names)
        # print('brands: ', brands)
        # print('self.fields before: ', self.fields)
        self.fields['brand'].choices = other_names
        # print('self.fields.items(): ', self.fields.items())
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
