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

