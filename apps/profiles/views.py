from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    context = { 'profile': request.user.profile }
    return render(request, 'profiles/dashboard.html', context)