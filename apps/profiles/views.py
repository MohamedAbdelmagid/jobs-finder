from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.jobs.models import Application
from apps.profiles.models import Message


@login_required
def dashboard(request):
    context = { 'profile': request.user.profile }
    return render(request, 'profiles/dashboard.html', context)

@login_required
def application(request, app_id):
    if request.user.profile.is_employer:
        application = get_object_or_404(Application, pk=app_id, job__employer=request.user)
    else:
        application = get_object_or_404(Application, pk=app_id, applicant=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message.objects.create(
                application=application,
                content=content,
                sender=request.user
            )
            return redirect('application', app_id=app_id)

    context = { 'application': application }
    return render(request, 'profiles/application.html', context)