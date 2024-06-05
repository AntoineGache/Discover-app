from django.contrib import admin
from .models import Message, Abonnement, Commentaire, Like, Publication

# Register your models here.

admin.site.register(Message)
admin.site.register(Abonnement)
admin.site.register(Commentaire)
admin.site.register(Like)
admin.site.register(Publication)
