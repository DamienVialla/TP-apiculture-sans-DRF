#Gestion des routes pour se connecter, se déconnecter et s'enregistrer
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

admin.site.site_header = "Projet Django Apiculture"

urlpatterns = [
    
    path('', include('principal.urls')), #idem avec les routes de l'urlpatterns de l'app principale
    path('admin/', admin.site.urls),#gestion admin, réalisé par django
    path('connexion/', include('accounts.urls')) # idem avec l'app accounts
]
