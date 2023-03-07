from django.contrib.auth.models import AbstractUser
from django.db import models

# la classe AbstractUser contient tous les éléments nécessaires pour gérer l'authentification
class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    follows = models.ManyToManyField('self',
                                     limit_choices_to={'role': CREATOR}, # seul les utilisateurs avec le role CREATOR puissent être suivis
                                     symmetrical=False,
                                     verbose_name='utilisateur'
                                     )
