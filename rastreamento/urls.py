from django.urls import path
from .views import index  # Certifique-se de importar a função correta

urlpatterns = [
    path('', index, name='home'),  # Defina a rota para a página inicial
]
