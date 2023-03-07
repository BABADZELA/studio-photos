# Generated by Django 4.1.7 on 2023-03-06 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_auto_20230306_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'CREATOR'}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]