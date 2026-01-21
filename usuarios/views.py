from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_dentistas')
def cadastrar_dentistas(request):
    if request.method == "GET":
        dentistas = Users.objects.filter(cargo="D")
        return render(request, 'cadastrar_dentistas.html', {'dentistas':dentistas})
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)
        if user.exists():

            #Utilizar messages do Django
            return HttpResponse('Email já existe')
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo='D')

        return HttpResponse('Conta Criada')
    
def login (request):
    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        
        return render(request, 'login.html' )
    
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user: 
            return HttpResponse('Usuário Inválido')
        
        auth.login(request, user)
        return HttpResponse('Usuário logado!')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_dentista')
def excluir_usuario(request, id):
    dentista= get_object_or_404(Users, id=id)
    dentista.delete()
    messages.add_message(request, messages.SUCCESS, 'Dentista Excluido com Sucesso!')
    return redirect(reverse('cadastrar_dentistas'))


# Create your views here.
