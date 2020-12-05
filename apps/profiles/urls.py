from django.urls import path

from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('application/<int:app_id>', views.application, name='application'),
    path('notifications', views.notifications, name='notifications'),
]