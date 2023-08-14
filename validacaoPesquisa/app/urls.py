from django.urls import re_path, path

from . import views
from .views import *

urlpatterns = [
    path(r'cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    path(r'listar_carro/', listar_carro, name='carro_list'),
    path(r'editar_carro/(?P<pk>[0-9]+)', editar_carro, name='editar_carro'),
    path(r'remover_carro/(?P<pk>[0-9]+)', remover_carro, name='remover_carro')
]
