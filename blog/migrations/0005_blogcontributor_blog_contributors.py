# Generated by Django 4.1.7 on 2023-03-06 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_photo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.CharField(blank=True, max_length=255)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('contributor', 'blog')},
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='blog.BlogContributor', to=settings.AUTH_USER_MODEL),
        ),
    ]