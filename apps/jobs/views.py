from django.shortcuts import render, get_object_or_404

from . models import Job


def job_view(request, id):
    job = get_object_or_404(Job, pk=id)

    context = { 'job': job }
    return render(request, 'jobs/job.html', context)
