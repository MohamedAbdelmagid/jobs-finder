from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from apps.jobs.models import Job


def index(request):
    jobs = Job.objects.all()

    context = { 'jobs': jobs }
    return render(request, 'core/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
        
    context = { 'form': form }
    return render(request, 'core/signup.html', context)
