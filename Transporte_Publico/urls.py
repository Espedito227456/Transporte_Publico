from django.contrib import admin
from django.urls import path, include  # Importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rastreamento.urls')),  # Inclui as URLs do seu aplicativo rastreamento
]
