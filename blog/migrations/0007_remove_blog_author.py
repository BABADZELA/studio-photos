# Generated by Django 4.1.7 on 2023-03-06 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230306_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]