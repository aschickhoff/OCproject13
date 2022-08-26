from django.test import TestCase
from django.urls import reverse


class LettingsTest(TestCase):
    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200
