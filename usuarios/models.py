from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser): #Herdando atributos de uma classe preexistente e colocando novos campos que dizem respeito a esse sistema em específico
    choices_cargo = (('D', 'Dentista'), ('S', 'Secretária'), ('A', 'Admin'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)
# Create your models here.
