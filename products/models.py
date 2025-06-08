from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=254)
    other_name = models.CharField(max_length=254)


    def __str__(serlf):
        return serlf.name
    
    def get_other_name(self):
        return self.other_name


class Product(models.Model):

    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL) # null
    sku = models.CharField(max_length=254, null=True, blank=True) # null

    name = models.CharField(max_length=254)
    display = models.CharField(max_length=254)
    processor = models.CharField(max_length=254)
    memory = models.CharField(max_length=254)
    storage = models.CharField(max_length=254)
    graphics = models.CharField(max_length=254)

    warranty = models.CharField(max_length=254, null=True, blank=True)# null
    operating_system = models.CharField(max_length=254, null=True, blank=True)# null

    availability = models.BooleanField(default=True, null=True, blank=True)# null
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)# null
    image_url = models.URLField(max_length=1024, null=True, blank=True)# null
    image = models.ImageField(null=True, blank=True)# null

    class Meta:

        ordering = ["sku"]
        #verbose_name_plural = "AllBrands"

    def __str__(self):
        return self.name