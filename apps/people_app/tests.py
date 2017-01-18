from django.test import TestCase
from django.shortcuts import render, redirect
from django.db import models
from .models import People


class People(TestCase):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def index(request):
        peoples = People.objects.all()
        context = {'peoples': peoples}
        return render(request, 'people_app/index.html', context)

    def create(request):
        print(request.POST)
        people_app = People(name=request.POST['name'], biography=request.POST['biography'])
        people_app.save()
        return redirect('/')

    
