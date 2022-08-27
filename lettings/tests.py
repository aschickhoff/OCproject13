from django.test import TestCase, Client
from django.urls import reverse

from .models import Address, Letting


class LettingsViewResponses(TestCase):
    @classmethod
    def setUp(self):
        self.c = Client()
        self.address = Address.objects.create(
            number=29,
            street='Sesamestreet',
            city='Sim City',
            state='CA',
            zip_code=12345,
            country_iso_code='CAL',
        )
        self.letting = Letting.objects.create(title='Utopia', address=self.address)

    def test_view_url_exists_at_desired_location(self):
        response = self.c.get('/lettings/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.c.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.c.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_view_displays_correct_title(self):
        response = self.c.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Lettings', 'Lettings')

    def test_view_displays_correct_content(self):
        response = self.c.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.content)
        self.assertIn(b'Profiles', response.content)

    def test_view_detail_url_accessible_by_name(self):
        response = self.c.get(reverse('lettings:letting', args=[self.letting.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_detail_uses_correct_template(self):
        response = self.c.get(reverse('lettings:letting', args=[self.letting.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_view_detail_displays_correct_title(self):
        response = self.c.get(reverse('lettings:letting', args=[self.letting.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Utopia', 'Utopia')

    def test_view_detail_displays_correct_content(self):
        response = self.c.get(reverse('lettings:letting', args=[self.letting.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sesamestreet', response.content)
        self.assertIn(b'Sim City', response.content)
        self.assertIn(b'CAL', response.content)
        self.assertIn(b'12345', response.content)
        self.assertIn(b'29', response.content)
        self.assertIn(b'Back', response.content)
        self.assertIn(b'Home', response.content)
        self.assertIn(b'Profiles', response.content)
