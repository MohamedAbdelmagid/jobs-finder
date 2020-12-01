from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.job_view, name='job'),
    path('new', views.new_job, name='new_job'),
]