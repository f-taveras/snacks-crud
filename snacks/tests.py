from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth.models import User


class SnacksTests(TestCase):
    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_status_code(self):
    # Create a test user (purchaser)
        user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

    # Now create a test snack object, setting the purchaser to the user you just created
        snack = Snack.objects.create(name='Test Snack', description='Test Description', purchaser=user)
    
        # Use the snack's id to construct the detail view URL
        url = reverse('snack_detail', args=[snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_snack_list_view_status_code(self):
        url = reverse('snack_list')  # Use the name of your URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_view_uses_correct_template(self):
        url = reverse('snack_list')  # Use the name of your URL pattern
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

   