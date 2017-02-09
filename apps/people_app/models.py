from django.db import models


# class Groups(models.Model):
#     name = models.CharField(max_length=255)
#     information = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=255)
    information = models.TextField(default="A normal group", null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class People(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
