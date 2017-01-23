from django.test import TestCase
from .models import People


class PeopleMethodTest(TestCase):
    def setUp(self):
        People.objects.create(name="lion", biography="roar")
        People.objects.create(name="cat", biography="meow")

    def test_people_and_biography(self):
        lion = People.objects.get(name="lion")
        cat = People.objects.get(name="cat")
        assert(lion.biography(),"roar")
        assert(cat.biography(), "meow")

    def test_edit_view(self):
        response = PeopleMethodTest.get('/edit/')
        assert response.status_code == 200