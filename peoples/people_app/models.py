from django.db import models
from django.utils import timezone

class People(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    created_at = models.DateTimeField(
            default=timezone.now)
    updated_at = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name