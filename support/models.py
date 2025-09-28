from django.db import models


class Faqs(models.Model):
    """
    Stores frequent questions and the answers
    """
    class Meta:
        verbose_name_plural = 'Faqs'

    question = models.CharField(max_length=254)
    answer = models.TextField(max_length=2000)

    def __str__(self):
        return self.answer
