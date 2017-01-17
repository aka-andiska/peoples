from django.shortcuts import render, redirect
from .models import People


def index(request):
    peoples = People.objects.all()
    context = {'peoples': peoples}
    return render(request, 'people_app/index.html', context)


def create(request):
    print(request.POST)
    people_app = People(name=request.POST['name'], biography=request.POST['biography'])
    people_app.save()
    return redirect('/')