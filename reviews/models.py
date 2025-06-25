from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-updated_on']

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_reviews')
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2,
                                 null=True, blank=True)
    review = models.TextField(null=False, blank=False, default='',
                              max_length=5000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} reviewed: {self.review}'
