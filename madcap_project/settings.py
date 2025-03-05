from pathlib import Path
import os
import dj_database_url
import logging
from django.utils.translation import gettext_lazy as _

# 📌 Détection de l'environnement
ENVIRONMENT = os.getenv("DJANGO_ENV", "local")  # "local" par défaut

# 📌 Base directory du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# 📌 Sécurité
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")  # 🔴 Change en prod !
DEBUG = ENVIRONMENT == "local"  # DEBUG=True seulement en local

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "madcap-70h2.onrender.com,madcap1874.onrender.com,127.0.0.1,localhost").split(",")

# 📌 Configuration Email (Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 📌 Applications installées
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "madcap_app",
]

# 📌 Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
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

# 📌 Base de données : SQLite en local, PostgreSQL en production
if ENVIRONMENT == "local":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
    }

# 📌 Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

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

# 📌 Gestion des fichiers statiques (CSS, JS, images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # Pour Render et collectstatic

if ENVIRONMENT == "local":
    STATICFILES_DIRS = [BASE_DIR / "static"]  # Assure-toi que ce dossier existe

# 📌 Gestion des fichiers médias
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 📌 Paramètres de langue et traductions
LANGUAGE_CODE = "fr"
LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('Anglais')),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

# 📌 Clé primaire par défaut
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
