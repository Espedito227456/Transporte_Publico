# Verifica se o ambiente virtual existe
if (Test-Path .\venv\Scripts\Activate.ps1) {
    # Ativa o ambiente virtual
    .\venv\Scripts\Activate.ps1
    
    # Inicia o servidor Django
    python manage.py runserver
} elseif (Test-Path .\venv\bin\activate) {
    # Para Linux/Mac, se necessário
    source ./venv/bin/activate
    
    # Inicia o servidor Django
    python manage.py runserver
} else {
    Write-Host "Ambiente virtual não encontrado. Por favor, crie um ambiente virtual."
}
