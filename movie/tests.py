from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Movie

class MovieTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        test_movie = Movie.objects.create(name='Thor', owner=testuser1, description='Test')

    def test_movie_model(self):
        movie = Movie.objects.get(id=1)
        actual_owner = str(movie.owner)
        actual_name = str(movie.name)
        actual_description = str(movie.description)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_name, 'Thor')
        self.assertEqual(actual_description, 'Test')
