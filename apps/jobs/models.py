from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    """ Model that represent job in database """

    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    employer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title