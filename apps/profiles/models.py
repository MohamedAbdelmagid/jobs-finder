from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Model that represent a user profile in the database """

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
