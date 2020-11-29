from django.urls import path
from django.contrib.auth import views as dj_views

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('logout', dj_views.LogoutView.as_view(), name='logout'),
]