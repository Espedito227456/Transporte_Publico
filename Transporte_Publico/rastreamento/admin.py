from django.contrib import admin
from .models import Linha, Onibus, Rota, PontoOnibus

class OnibusInline(admin.TabularInline):
    model = Onibus
    extra = 1  # Número de formulários em branco a serem exibidos

class LinhaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'descricao')  # Campos que serão exibidos na lista
    search_fields = ('numero', 'descricao')      # Campos que podem ser pesquisados
    fields = ('numero', 'descricao')              # Campos que podem ser editados na página de edição
    list_filter = ('descricao',)                   # Permite filtrar as linhas por descrição, se desejado
    ordering = ('numero',)   

class OnibusAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'capacidade_sentados', 'capacidade_em_pe', 'linha')  # Campos a serem exibidos
    search_fields = ('numero', 'linha__numero')  # Permite buscar ônibus pelo número e pela linha associada
    list_filter = ('linha',)  # Filtrar ônibus por linha
    fields = ('numero', 'capacidade_sentados', 'capacidade_em_pe', 'linha')  # Campos editáveis

class RotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ponto_inicio', 'ponto_fim')
    search_fields = ('nome',)
    fields = ('nome', 'ponto_inicio', 'ponto_fim')

class PontoOnibusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')  # Certifique-se de que 'rota' não está aqui
    search_fields = ('nome',)
    filter_horizontal = ('linhas',)  # Para selecionar múltiplas linhas de forma fácil

# Registrando os modelos no admin
admin.site.register(Linha, LinhaAdmin)
admin.site.register(Onibus, OnibusAdmin)
admin.site.register(Rota, RotaAdmin)
admin.site.register(PontoOnibus, PontoOnibusAdmin)
