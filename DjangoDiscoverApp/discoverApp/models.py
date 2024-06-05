from django.db import models
from django.conf import settings

# Create your models here.

class Publication(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    publieur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.titre
      
class Message(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    envoyeur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='envoyeur', on_delete=models.CASCADE)
    receveur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receveur', on_delete=models.CASCADE)
    date = models.DateField()
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Commentaire(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.text

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Abonnement(models.Model):
    abonne = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='abonne', on_delete=models.CASCADE)
    abonnement = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='abonnement', on_delete=models.CASCADE)
