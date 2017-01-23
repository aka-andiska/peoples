from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)