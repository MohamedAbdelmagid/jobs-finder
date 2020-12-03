from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . models import Job
from . forms import NewJobForm, ApplicationForm


def job_view(request, id):
    job = get_object_or_404(Job, pk=id)

    context = { 'job': job }
    return render(request, 'jobs/job.html', context)

@login_required
def new_job(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = NewJobForm()

    context = { 'form': form }
    return render(request, 'jobs/new_job.html', context)

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.save()

            return redirect('dashboard')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'jobs/apply_for_job.html', context)

@login_required
def job_dashboard(request, job_id):
    job = get_object_or_404(Job, pk=job_id, employer=request.user)

    context = { 'job': job }
    return render(request, 'jobs/job_dashboard.html', context)