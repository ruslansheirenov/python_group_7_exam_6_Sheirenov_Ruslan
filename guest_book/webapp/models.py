from django.db import models

# Create your models here.

class Guest_book(models.Model):
    author = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    content = models.TextField(max_length=3000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField(max_length=7, null=False, blank=False)