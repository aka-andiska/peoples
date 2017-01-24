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
        create should creating new peoples and display in index
        """





