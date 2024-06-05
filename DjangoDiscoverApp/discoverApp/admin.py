from django.contrib import admin
from .models import Message, Abonnement, Publication, Commentaire, Like

# Register your models here.

admin.site.register(Message)
admin.site.register(Abonnement)
admin.site.register(Publication)
admin.site.register(Commentaire)
admin.site.register(Like)