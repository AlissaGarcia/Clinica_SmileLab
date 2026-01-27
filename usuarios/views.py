from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth, messages
from rolepermissions.decorators import has_permission_decorator
from .models import Users, Paciente, Agendamento
from rolepermissions.decorators import has_role_decorator



# LOGIN / LOGOUT


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # Se já estiver logado, manda direto para o dashboard correto
            if request.user.cargo == 'S':
                return redirect(reverse('dashboard_secretaria'))
            elif request.user.cargo == 'D':
                return redirect(reverse('dashboard_dentista'))
            else:
                return redirect(reverse('dashboard_admin'))

        return render(request, 'login.html')

    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=email, password=senha)

        if not user:
            return HttpResponse('Usuário inválido')

        auth.login(request, user)

        if user.cargo == 'S':
            return redirect(reverse('dashboard_secretaria'))
        elif user.cargo == 'D':
            return redirect(reverse('dashboard_dentista'))
        else:
            return redirect(reverse('dashboard_admin'))



def logout(request):
    request.session.flush()
    return redirect(reverse('login'))



# DENTISTAS


@has_permission_decorator('cadastrar_dentistas')
def cadastrar_dentistas(request):
    if request.method == "GET":
        dentistas = Users.objects.filter(cargo="D")
        return render(request, 'cadastrar_dentistas.html', {'dentistas': dentistas})

    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Users.objects.filter(email=email).exists():
            messages.error(request, 'Email já existe')
            return redirect(reverse('cadastrar_dentistas'))

        Users.objects.create_user(username=email, email=email, password=senha, cargo='D')
        messages.success(request, 'Dentista cadastrado com sucesso!')
        return redirect(reverse('cadastrar_dentistas'))


@has_permission_decorator('cadastrar_dentista')
def excluir_dentista(request, id):
    dentista = get_object_or_404(Users, id=id, cargo='D')
    dentista.delete()
    messages.success(request, 'Dentista excluído com sucesso!')
    return redirect(reverse('cadastrar_dentistas'))


# SECRETÁRIOS


@has_permission_decorator('cadastrar_secretarios')
def cadastrar_secretarios(request):
    if request.method == "GET":
        secretarios = Users.objects.filter(cargo="S")
        return render(request, 'cadastrar_secretarios.html', {'secretarios': secretarios})

    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Users.objects.filter(email=email).exists():
            messages.error(request, 'Esse email já existe!')
            return redirect(reverse('cadastrar_secretarios'))

        Users.objects.create_user(username=email, email=email, password=senha, cargo='S')
        messages.success(request, 'Secretário(a) criado com sucesso!')
        return redirect(reverse('cadastrar_secretarios'))


@has_permission_decorator('cadastrar_secretario')
def excluir_secretario(request, id):
    secretario = get_object_or_404(Users, id=id, cargo='S')
    secretario.delete()
    messages.success(request, 'Secretário(a) excluído com sucesso!')
    return redirect(reverse('cadastrar_secretarios'))






# DASHBOARDS


@has_permission_decorator('dashboard_secretaria')
def dashboard_secretaria(request):
    pacientes = Paciente.objects.all()
    agendamentos = Agendamento.objects.all()
    return render(request, 'dashboard_secretaria.html', {
        'pacientes': pacientes,
        'agendamentos': agendamentos
    })


@has_permission_decorator('dashboard_dentista')
def dashboard_dentista(request):
    agendamentos = Agendamento.objects.filter(dentista=request.user)
    return render(request, 'dashboard_dentista.html', {
        'agendamentos': agendamentos
    })



# PACIENTES


@has_permission_decorator('cadastrar_pacientes')
def cadastrar_pacientes(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        return render(request, 'cadastrar_pacientes.html', {'pacientes': pacientes})

    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        observacao = request.POST.get('observacao')

        if Paciente.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado!')
            return redirect(reverse('cadastrar_pacientes'))

        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            endereco=endereco,
            telefone=telefone,
            data_nascimento=data_nascimento,
            observacao=observacao
        )

        messages.success(request, 'Paciente cadastrado com sucesso!')
        return redirect(reverse('cadastrar_pacientes'))


@has_permission_decorator('cadastrar_pacientes')
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    messages.success(request, 'Paciente excluído com sucesso!')
    return redirect(reverse('cadastrar_pacientes'))



# AGENDAMENTOS


@has_permission_decorator('criar_agendamentos')
def agendamentos(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        dentistas = Users.objects.filter(cargo="D")
        agendamentos = Agendamento.objects.all()

        return render(request, 'agendamentos.html', {
            'pacientes': pacientes,
            'dentistas': dentistas,
            'agendamentos': agendamentos
        })

    if request.method == "POST":
        paciente_id = request.POST.get('paciente')
        dentista_id = request.POST.get('dentista')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        procedimento = request.POST.get('procedimento')

        paciente = get_object_or_404(Paciente, id=paciente_id)
        dentista = get_object_or_404(Users, id=dentista_id, cargo='D')

        Agendamento.objects.create(
            paciente=paciente,
            dentista=dentista,
            data=data,
            horario=horario,
            procedimento=procedimento
        )

        messages.success(request, 'Agendamento realizado com sucesso!')
        return redirect(reverse('agendamentos'))


@has_permission_decorator('criar_agendamentos')
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    messages.success(request, 'Agendamento excluído com sucesso!')
    return redirect(reverse('agendamentos'))


@has_role_decorator('admin')
def dashboard_admin(request):
    return render(request, 'adm.html')

