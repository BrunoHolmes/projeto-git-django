from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario


def index(request):

    contexto = {
        'nome_pessoa': 'Bruno Holmes de Albuquerque',
        'endereço_pessoa': 'Felix de Brito e Melo',
        'cidade_pessoa': 'Recife'
    }

    return render(request, "home.html", contexto)
