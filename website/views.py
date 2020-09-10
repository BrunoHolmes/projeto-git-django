from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # htttp://localhost:8000/funcionario/views_1/

    print('Entramos na view 😁')

    return render(request, "home.html")
