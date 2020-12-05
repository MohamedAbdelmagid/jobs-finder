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

class Notification(models.Model):
    """ Model that represent a notification in the database """

    MESSAGE = 'message'
    APPLICATION = 'application'

    TYPES = (
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
    )

    which = models.CharField(max_length=20, choices=TYPES)
    is_seen = models.BooleanField(default=False)
    identifier = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='created_notifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
