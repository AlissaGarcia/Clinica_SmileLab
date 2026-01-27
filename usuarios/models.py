from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    choices_cargo = (('D', 'Dentista'), ('S', 'Secretária'), ('A', 'Admin'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)



class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        limit_choices_to={'cargo': 'D'}
    )
    data = models.DateField()
    horario = models.TimeField()
    procedimento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.horario}"
