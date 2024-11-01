"""
Django settings for Transporte_Público project.

Gerado por 'django-admin startproject' usando Django 5.1.2.
"""

from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta do Django. Mantenha-a em segredo em produção!
SECRET_KEY = 'django-insecure-7(x-pj0)o^=n%3bx7c-zd+d17r9plh0=kwsico+d0uhvk0gri!'

# Modo de depuração. Não ative em produção!
DEBUG = True

# Lista de hosts permitidos
ALLOWED_HOSTS = []

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',              # Admin do Django
    'django.contrib.auth',               # Sistema de autenticação
    'django.contrib.contenttypes',       # Tipos de conteúdo
    'django.contrib.sessions',           # Gerenciamento de sessões
    'django.contrib.messages',            # Sistema de mensagens
    'django.contrib.staticfiles',        # Arquivos estáticos
    'rastreamento',                      # Seu aplicativo rastreamento
]

# Middleware que processa as requisições
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs de configuração
ROOT_URLCONF = 'Transporte_Publico.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '../templates'],  # Altere para apontar para a pasta templates na raiz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Aplicação WSGI
WSGI_APPLICATION = 'Transporte_Publico.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Usando SQLite
        'NAME': BASE_DIR / 'db.sqlite3',          # Localização do banco de dados
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de internacionalização
LANGUAGE_CODE = 'en-us'  # Código de idioma
TIME_ZONE = 'UTC'        # Fuso horário
USE_I18N = True          # Habilitar internacionalização
USE_TZ = True            # Habilitar fuso horário

# Arquivos estáticos (CSS, JavaScript, Imagens)
STATIC_URL = 'static/'   # URL para arquivos estáticos

# Campo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Tipo de chave primária padrão
