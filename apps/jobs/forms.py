from django import forms

from . models import Job


class NewJobForm(forms.ModelForm):
    """ Form for creating new job """

    class Meta:
        model = Job
        fields = ['title', 'description', 'details']