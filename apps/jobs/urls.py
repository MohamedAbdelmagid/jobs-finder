from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.job_view, name='job'),
    path('new', views.new_job, name='new_job'),
    path('<int:job_id>/apply', views.apply_for_job, name='apply_for_job'),
    path('<int:job_id>/dashboard', views.job_dashboard, name='job_dashboard'),
]