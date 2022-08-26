from django.test import TestCase
from django.urls import reverse


class ProfilesTest(TestCase):
    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200
