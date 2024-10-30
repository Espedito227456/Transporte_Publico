from django.shortcuts import render

def index(request):  # ou 'home', dependendo do que você está usando
    context = {
        'titulo': 'Página Inicial do Transporte Público',
        'mensagem': 'Bem-vindo ao sistema de transporte público!',
    }
    return render(request, 'index.html', context)
