from django.test import TestCase
from .models import People


class PeopleMethodTest(TestCase):
    def setUp(self):
        People.objects.create(name="lion", biography="roar")
        People.objects.create(name="cat", biography="meow")

    def test_people_and_biography(self):
        lion = People.objects.get(name="lion")
        cat = People.objects.get(name="cat")
        self.assertIs(lion.biography())
        self.assertIs(cat.biography())