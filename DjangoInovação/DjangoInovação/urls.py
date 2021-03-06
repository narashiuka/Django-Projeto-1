﻿"""
Definition of urls for DjangoInovação.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/DjangoProjeto/')),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('DjangoProjeto/', views.ListaEventos),
    path('DjangoProjeto/lista/<int:id_usuario>/', views.json_lista_evento),
    path('DjangoProjeto/evento/', views.evento),
    path('DjangoProjeto/evento/submit', views.submit_evento),
    path('DjangoProjeto/delete/<int:id_evento>/', views.delete_evento),
    path('loginOne/', views.login_user),
    path('loginOne/submit', views.submit_login),
    path('DjangoProjeto/deslogarOne/', views.logout_user),
    path('DjangoProjeto/evento/deslogarOne/', views.logout_user),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
