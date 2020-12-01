from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    """ Model that represent job in database """

    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    employer = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Application(models.Model):
    """ Model that represent user application for a job in database """

    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    applicant = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
