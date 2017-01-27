from django.shortcuts import render, redirect
from .models import People, Group


def index(request):
    peoples = People.objects.all()
    groups = Group.objects.all()
    group_1 = People.objects.filter(group=1)
    group_2 = People.objects.filter(group=2)
    context = {'peoples': peoples, 'groups': groups, 'group_1': group_1, 'group_2': group_2}

    return render(request, 'people_app/index.html', context)

def create(request):
    print(request.POST)
    group_instance = Group.objects.get(pk=request.POST['group'])
    people_app = People(name=request.POST['name'], biography=request.POST['biography'], group=group_instance)
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

def destroy(request, id):
    people = People.objects.get(id=id)
    people.delete()
    return redirect('/')

