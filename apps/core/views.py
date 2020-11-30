from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from apps.jobs.models import Job
from apps.profiles.models import Profile


def index(request):
    jobs = Job.objects.all()

    context = { 'jobs': jobs }
    return render(request, 'core/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            account_type = request.POST.get('account_type', 'hunter')
            if account_type == 'employer':
                user_profile = Profile.objects.create(user=user, is_employer=True)
            else:
                user_profile = Profile.objects.create(user=user)
            user_profile.save()

            auth.login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
        
    context = { 'form': form }
    return render(request, 'core/signup.html', context)
