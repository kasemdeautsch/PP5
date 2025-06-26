from django.db import models

# Create your models here.


class Faqs(models.Model):

    class Meta:
        verbose_name_plural = 'Faqs'

    question = models.CharField(max_length=254)
    answer = models.TextField(max_length=2000)

    def __str__(self):
        return self.answer