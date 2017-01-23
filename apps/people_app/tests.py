from django.test import TestCase
import datetime

from django.utils import timezone
from .models import People


class PeopleMethodTest(TestCase):
    def setUp(self):
        People.objects.create(name="lion", biography="roar")
        People.objects.create(name="cat", biography="meow")

    def test_people_and_biography(self):
        lion = People.objects.get(name="lion")
        cat = People.objects.get(name="cat")
        self.assertIs(lion.biography(), 'The lion says "roar"')
        self.assertIs(cat.biography(), 'The cat says "meow"')