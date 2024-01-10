#Gestion des routes pour se connecter, se déconnecter et s'enregistrer

from django.urls import path
from . import views

app_name = "accounts"
#path(chemin,fonction,nom)
urlpatterns = [
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
]
