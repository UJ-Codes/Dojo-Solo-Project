from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('about', views.about),
    path('login_page', views.login_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('account', views.account),
    path('schedule', views.schedule),
    path('update', views.update),
    path('consult', views.work),
    path('location', views.location),
    path('review', views.review),
    path('create_wish', views.create_wish),
]