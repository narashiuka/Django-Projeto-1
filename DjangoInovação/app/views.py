"""
Definition of views.
"""

from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def index(request):
    return redirect('/DjangoProjeto/')

def login_user(request):
    return render(request, 'loginOne.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválidos")
    return redirect('/')

@login_required(login_url='/loginOne/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/loginOne/')
def ListaEventos(request):
    utilizador = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    event = Evento.objects.filter(Usuario=utilizador,
                                  data_evento__gt=data_atual)
    dados = {'eventos': event}
    return render(request, 'DjangoProjeto.html', dados)

@login_required(login_url='/loginOne/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       data_evento=data_evento,
                                                       descricao=descricao,
                                                       local=local)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario,
                                  local=local)
    return redirect('/')

@login_required(login_url='/loginOne/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception():
        raise Http404()
    if (usuario == evento.Usuario):
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

@login_required(login_url='/loginOne/')
def json_lista_evento(request, id_usuario):
    utilizador = User.objects.get(id=id_usuario)
    event = Evento.objects.filter(Usuario=utilizador).values('id', 'titulo')
    return JsonResponse(list(event), safe=False)