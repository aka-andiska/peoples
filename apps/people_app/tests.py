from django.test import TestCase
from .models import People, Group

from django.core.urlresolvers import reverse

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

    def test_group(self):
        """
        group can select data people by group id from table people
        """
        people_in_group_1 = People.objects.filter(group_id=1)
        people_in_group_2 = People.objects.filter(group_id=2)

        self.assertNotIn(people_in_group_1, people_in_group_2)

    def test_create_in_group(self):
        """
        group can create new data
        """
        









