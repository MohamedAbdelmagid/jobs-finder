from django.db import models
from django.contrib.auth.models import User

from apps.jobs.models import Application


class Profile(models.Model):
    """ Model that represent a user profile in the database """

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

class Message(models.Model):
    """ Model that represent a message in the database """

    content = models.TextField()
    application = models.ForeignKey(Application, related_name='messages', on_delete=models.CASCADE)

    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    sended_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sended_at']
