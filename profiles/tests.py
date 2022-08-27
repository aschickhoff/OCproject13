from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profile


class ProfilesViewResponses(TestCase):
    @classmethod
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create(
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@testxyz.com',
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city='Doe City')

    def test_view_url_exists_at_desired_location(self):
        response = self.c.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.c.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.c.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_view_displays_correct_title(self):
        response = self.c.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Profiles', 'Profiles')

    def test_view_displays_correct_content(self):
        response = self.c.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.content)
        self.assertIn(b'Lettings', response.content)

    def test_view_detail_url_accessible_by_name(self):
        response = self.c.get(reverse('profiles:profile', args=['JohnDoe']))
        self.assertEqual(response.status_code, 200)

    def test_view_detail_uses_correct_template(self):
        response = self.c.get(reverse('profiles:profile', args=['JohnDoe']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_view_detail_displays_correct_title(self):
        response = self.c.get(reverse('profiles:profile', args=['JohnDoe']))
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('JohnDoe', 'JohnDoe')

    def test_view_detail_displays_correct_content(self):
        response = self.c.get(reverse('profiles:profile', args=['JohnDoe']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'JohnDoe', response.content)
        self.assertIn(b'John', response.content)
        self.assertIn(b'Doe', response.content)
        self.assertIn(b'johndoe@testxyz.com', response.content)
        self.assertIn(b'Doe City', response.content)
        self.assertIn(b'Back', response.content)
        self.assertIn(b'Home', response.content)
        self.assertIn(b'Lettings', response.content)
