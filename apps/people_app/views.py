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


def edit(request, id):
    people = People.objects.get(id=id)
    context = {'people': people}
    return render(request, 'people_app/edit.html', context)

def update(request, id):
    people = People.objects.get(id=id)
    people.name = request.POST['name']
    people.biography = request.POST['biography']
    people.save()
    return redirect('/')

