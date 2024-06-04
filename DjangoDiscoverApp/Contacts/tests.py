from django.test import TestCase
from django.contrib.auth import get_user_model
from discoverApp.models import Message, Abonnement
import datetime

# Create your tests here.

User = get_user_model()

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')

    def test_message_creation(self):
        message = Message.objects.create(
            id=1,
            envoyeur=self.user1,
            receveur=self.user2,
            date=datetime.date.today(),
            text='Test message'
        )
        self.assertEqual(str(message), 'Test message')

    def test_message_str_representation(self):
        message = Message.objects.create(
            id=1,
            envoyeur=self.user1,
            receveur=self.user2,
            date=datetime.date.today(),
            text='Test message'
        )
        self.assertEqual(str(message), 'Test message')

class AbonnementModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')

    def test_abonnement_creation(self):
        abonnement = Abonnement.objects.create(
            abonne=self.user1,
            abonnement=self.user2
        )
        self.assertEqual(abonnement.abonne, self.user1)
        self.assertEqual(abonnement.abonnement, self.user2)
