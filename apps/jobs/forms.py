from django import forms

from . models import Job, Application


class NewJobForm(forms.ModelForm):
    """ Form for creating new job """

    class Meta:
        model = Job
        fields = ['title', 'description', 'details']

class ApplicationForm(forms.ModelForm):
    """ Form for applying for a job """

    class Meta:
        model = Application
        fields = ['content', 'experience']