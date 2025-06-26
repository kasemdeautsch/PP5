from django.db import models

# Blog post model


class About(models.Model):
    """Stores a single about record"""
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

#  Blog post model


class CollaborateRequest(models.Model):
    """Stores a single collaborate request"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Collaboration request from: {self.name}'
    