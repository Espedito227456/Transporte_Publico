from django.shortcuts import render, redirect
from .forms import RotaForm, LinhaForm, OnibusForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def create_rota(request):
    if request.method == "POST":
        form = RotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RotaForm()
    return render(request, 'create_rota.html', {'form': form})

def create_linha(request):
    if request.method == "POST":
        form = LinhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LinhaForm()
    return render(request, 'create_linha.html', {'form': form})

def create_onibus(request):
    if request.method == "POST":
        form = OnibusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OnibusForm()
    return render(request, 'create_onibus.html', {'form': form})

def destino(request):
    if request.method == 'POST':
        origem = request.POST.get('origem')
        destino = request.POST.get('destino')

        # Chamar a API do Google Maps para obter a rota
        api_key = settings.GOOGLE_API_KEY  # Certifique-se de que sua chave da API do Google está configurada no settings.py
        url = "https://maps.googleapis.com/maps/api/directions/json"
        
        params = {
            'origin': origem,
            'destination': destino,
            'key': api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == 'OK':
            # Supondo que você queira passar as informações de rota para o template
            route = data['routes'][0]['legs'][0]
            duration = route['duration']['text']
            distance = route['distance']['text']
            # Você pode adicionar mais informações como etapas da rota, se necessário
            return render(request, 'destino.html', {
                'origem': origem,
                'destino': destino,
                'duration': duration,
                'distance': distance,
                'map_data': data  # Passa o JSON de dados da rota para o template
            })
        else:
            # Em caso de erro
            return render(request, 'destino.html', {
                'error': "Não foi possível calcular a rota."
            })
    else:
        return render(request, 'destino.html')


