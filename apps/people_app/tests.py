from django.test import TestCase

from .models import People, Group

from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory, force_authenticate


class PeopleMethodTest(TestCase):
    def test_index(self):
        """
        Index should display all peoples
        """
        lion = People.objects.create(name="lion", biography="roar") #this how to arrange
        cat = People.objects.create(name="cat", biography="meow")

        response = self.client.get(reverse('index')) #this is how to act

        self.assertEqual(response.status_code, 200) #this is how to assert
        self.assertEqual(len(response.context['peoples']),2)
        self.assertEqual(response.context['peoples'][0], lion)
        self.assertEqual(response.context['peoples'][1], cat)


    def test_create(self):
        """
        crete should can creating new data and post in index
        """
        cat = People.objects.create(name="cat", biography="meow")

        response = self.client.post(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['peoples'][0], cat)


    def test_edit(self):
        """
        edit can be editing data and get by id
        """
        peoples = People.objects.all()
        edit_lion = People.objects.filter(id=1)

        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(edit_lion, peoples)


    def test_update(self):
        """
        update can be post data to index after editing by id
        """
        people = People.objects.all()
        to_update = People.objects.filter(id=1)

        response = self.client.post(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(to_update, people)


    def test_delete(self):
        """
        delete can deleting data by id
        """
        to_delete = People.objects.filter(id=2)
        peoples = People.objects.all()
        self.assertNotIn(to_delete, peoples)


    def test_group_detail(self):
        """
        group can select data people by id from table people
        """
        people_in_group_1 = People.objects.filter(group_id=1)
        people_in_group_2 = People.objects.filter(group_id=2)

        self.assertNotIn(people_in_group_1, people_in_group_2)


    def tes_group_create(self):
        """
         Create_Group can create new group
        """
        test = Group.objects.create(name="test", information="testing")

        response = self.client.post(reverse('group_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['group'][0], test)


    def test_group_update(self):
        """
        update can be post data group to group list after editing
        """
        group1 = Group.objects.all()
        to_update = Group.objects.filter(id=1)

        response = self.client.post(reverse('group_list'))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(to_update, group1)


    def test_group_delete(self):
        """
        delete can deleting group by id
        """
        to_delete = Group.objects.filter(id=2)
        groups = Group.objects.all()
        self.assertNotIn(to_delete, groups)











