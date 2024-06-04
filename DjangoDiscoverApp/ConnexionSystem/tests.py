from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your tests here.

class SignInViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_signin_view_get(self):
        response = self.client.get(reverse('ConnexionSystem:signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin/signin.html')

    def test_signin_view_post_valid_credentials(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('ConnexionSystem:signin'), data)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

    def test_signin_view_post_invalid_credentials(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('ConnexionSystem:signin'), data)
        self.assertRedirects(response, reverse('ConnexionSystem:signin'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

class SignOutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_signout_view_post(self):
        response = self.client.post(reverse('ConnexionSystem:signout'))
        self.assertRedirects(response, reverse('ConnexionSystem:signin'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view_get(self):
        response = self.client.get(reverse('ConnexionSystem:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_register_view_post_valid_data(self):
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword', 'password2': 'newpassword'}
        response = self.client.post(reverse('ConnexionSystem:register'), data)
        self.assertRedirects(response, reverse('ConnexionSystem:signin'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

    def test_register_view_post_existing_username(self):
        User.objects.create_user(username='existinguser', password='testpassword')
        data = {'username': 'existinguser', 'email': 'newuser@example.com', 'password': 'newpassword', 'password2': 'newpassword'}
        response = self.client.post(reverse('ConnexionSystem:register'), data)
        self.assertRedirects(response, reverse('ConnexionSystem:register'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

    def test_register_view_post_existing_email(self):
        User.objects.create_user(username='existinguser', email='existingemail@example.com', password='testpassword')
        data = {'username': 'newuser', 'email': 'existingemail@example.com', 'password': 'newpassword', 'password2': 'newpassword'}
        response = self.client.post(reverse('ConnexionSystem:register'), data)
        self.assertRedirects(response, reverse('ConnexionSystem:register'))
        self.assertTrue(messages.get_messages(response.wsgi_request))

    def test_register_view_post_mismatched_passwords(self):
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword', 'password2': 'wrongpassword'}
        response = self.client.post(reverse('ConnexionSystem:register'), data)
        self.assertRedirects(response, reverse('ConnexionSystem:register'))
        self.assertTrue(messages.get_messages(response.wsgi_request))