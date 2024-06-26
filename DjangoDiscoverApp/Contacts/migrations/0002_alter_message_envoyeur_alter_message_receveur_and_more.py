# Generated by Django 5.0.3 on 2024-06-03 17:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='envoyeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envoyeur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='receveur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receveur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abonne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abonne', to=settings.AUTH_USER_MODEL)),
                ('abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abonnement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
