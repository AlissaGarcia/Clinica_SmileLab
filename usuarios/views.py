from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_dentistas')
def cadastrar_dentistas(request):
    return render(request, 'cadastrar_dentistas.html')

# Create your views here.
