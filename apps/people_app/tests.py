from django.test import TestCase
from .models import People

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
        lion = People.objects.create(name="lion", biography="roar")
        cat = People.objects.create(name="cat", biography="meow")
        response = self.client.post(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['peoples']),2)

    def test_edit(self):
        to_edit = People.objects.filter(id=1)
        peoples = People.objects.all()

        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(to_edit, peoples)



    def test_update(self):
        pass



    def test_delete(self):
        """
        delete can deleting data by id
        """
        to_delete = People.objects.filter(id=2).delete()
        peoples = People.objects.all()
        self.assertNotIn(to_delete, peoples)








