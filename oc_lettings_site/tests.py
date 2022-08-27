from django.test import TestCase, Client
from django.urls import reverse


class LandingPageTest(TestCase):
    @classmethod
    def setUp(self):
        self.c = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_displays_correct_title(self):
        response = self.c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Holiday Homes', 'Holiday Homes')

    def test_view_displays_correct_content(self):
        response = self.c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Profile', response.content)
        self.assertIn(b'Lettings', response.content)
