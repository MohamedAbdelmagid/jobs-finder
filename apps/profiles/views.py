from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.jobs.models import Application
from apps.profiles.models import Message, Notification
from apps.profiles.utilities import create_notification


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
            if request.user.profile.is_employer:
                create_notification(request, application.applicant, 'message', identifier=application.id)
            else:
                create_notification(request, application.job.employer, 'message', identifier=application.id)

            return redirect('application', app_id=app_id)

    context = { 'application': application }
    return render(request, 'profiles/application.html', context)

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_seen = True
        notification.save()

        if notification.which == Notification.MESSAGE:
            return redirect('application', app_id=notification.identifier)
        elif notification.which == Notification.APPLICATION:
            return redirect('application', app_id=notification.identifier)

    return render(request, 'profiles/notifications.html')
