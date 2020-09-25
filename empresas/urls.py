from . import views
from django.urls import path, include

app_name = 'empresas'

urlpatterns = [
    path('cadastro', views.cadastro, name = 'cadastro'),
    #path('listar', views.listar, name='cadastro'),
    #path('editar', views.editar, name='cadastro'),
    #path('excluir', views.excluir, name='cadastro')
]