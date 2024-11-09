from django.urls import path
from .views import index, create_rota, create_linha, create_onibus, destino

urlpatterns = [
    path('', index, name='index'),
    path('create-rota/', create_rota, name='create_rota'),
    path('create-linha/', create_linha, name='create_linha'),
    path('create-onibus/', create_onibus, name='create_onibus'),
    path('destino/', destino, name='destino'),
]
