from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Empresas
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        response = {
            'response': HTTP_200_OK,
        }

        return JsonResponse(response)
