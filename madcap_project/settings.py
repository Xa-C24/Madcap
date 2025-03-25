from pathlib import Path
import os
import dj_database_url
import logging
from django.utils.translation import gettext_lazy as _



# 📌 Détection de l'environnement
ENVIRONMENT = os.getenv("DJANGO_ENV", "local")  # "local" par défaut

# 📌 Configuration SMTP Gmail pour envoyer des emails en local et production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # Récupère depuis .env
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # Récupère depuis .env
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 📌 Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 📌 Sécurité
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")  # --🔴 Change cette valeur en production !--
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "madcap-70h2.onrender.com,madcap1874.onrender.com,127.0.0.1,localhost").split(",")


# 📌 Applications installées
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "madcap_app",

    # Cloudinary
    #"cloudinary",
    #"cloudinary_storage",
]

# 📌 Middleware (ajout de Whitenoise pour Render)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  #  Ajout pour gérer les fichiers statiques sur Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 📌 URLs
ROOT_URLCONF = "madcap_project.urls"

# 📌 Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

# 📌 WSGI
WSGI_APPLICATION = "madcap_project.wsgi.application"

# 📌 Base de données (PostgreSQL sur Render)
# DATABASES = {
   # "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
# }

# Base de donnée en local

if ENVIRONMENT == "local":
    # Base locale (pour ton ordi)
    print("🎯 Base locale activée")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "madcapdb",
            "USER": "madcapuser",
            "PASSWORD": "Basededonnemadcap",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
else:
    print("🌐 Base distante activée (Render/Supabase)")
    # Base distante (en ligne, sur Render)
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}



# 📌 Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 📌 Configuration Email (exemple avec Gmail)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

# 📌 Logs
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# 📌 Fuseau horaire et localisation
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📌 Gestion des fichiers statiques. (CSS, JS, images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  #  Optimisation pour Render

# 📌 Gestion des fichiers médias (images uploadées)
DEBUG = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 📌 Paramètres de langue
LANGUAGE_CODE = "fr"
LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('Anglais')),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

# 📌 Clé primaire par défaut
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 📌 Port (utile pour Render)
PORT = os.getenv("PORT", "8000")

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backups'}