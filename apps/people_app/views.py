from django.shortcuts import render, redirect
from .models import People, Group


def index(request):
    peoples = People.objects.all()
    groups = Group.objects.all()
    group_1 = People.objects.filter(group=1)
    group_2 = People.objects.filter(group=2)
    group_3 = People.objects.filter(group=3)
    context = {'peoples': peoples, 'groups': groups, 'group_1': group_1, 'group_2': group_2, 'group_3': group_3}

    return render(request, 'people_app/index.html', context)

def create(request):
    group_instance = Group.objects.get(pk=request.POST['group'])
    people_app = People(name=request.POST['name'], biography=request.POST['biography'], group=group_instance)
    people_app.save()
    return redirect('/')

def edit(request, id):
    people = People.objects.get(id=id)
    groups = Group.objects.all()
    group_1 = People.objects.filter(group=1)
    group_2 = People.objects.filter(group=2)
    group_3 = People.objects.filter(group=3)
    context = {'people': people, 'groups': groups, 'group_1': group_1, 'group_2': group_2, 'group_3': group_3}

    return render(request, 'people_app/edit.html', context)

def update(request, id):
    people = People.objects.get(id=id)
    group_id = request.POST['group']
    if group_id is "":
        group_id = people.group.id
    group_instance = Group.objects.get(id=group_id)
    people.name = request.POST['name']
    people.biography = request.POST['biography']
    people.group = group_instance
    people.save()
    return redirect('/')

def destroy(request, id):
    people = People.objects.get(id=id)
    people.delete()
    return redirect('/')



def group(request, id):
    group = Group.objects.get(pk=id)
    group_1 = People.objects.filter(group=id)
    context = {'group': group, 'group_1': group_1}
    return render(request, 'people_app/group.html', context)

def group_list(request):
    group_list = Group.objects.all()
    context = {'group_list': group_list}
    return render(request, 'people_app/groupall.html', context)

# def create_group(request):
#     group_instance = Group.objects.get(pk=request.POST['group'])
#     people_app = Group(name=request.POST['name'], information=request.POST['information'], group=group_instance)
#     people_app.save()
#     return redirect('/')

# defback(request):
#     peoples = People.objects.all()
#     groups = Group.objects.all()
#     context = {'peoples': peoples, 'groups': groups}
#
#     return redirect(request, 'people_app/index.html', context)