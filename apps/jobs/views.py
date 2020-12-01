from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . models import Job
from . forms import NewJobForm


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