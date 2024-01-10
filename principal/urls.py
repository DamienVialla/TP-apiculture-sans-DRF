from django.urls import path
from principal import views

#défini où se situe le début de l'arborescence
app_name = "principal"

#gère les url de l'application
urlpatterns = [
    path('',views.PagePrincipale, name = 'index'),
    path('<int:ruche_id>/',views.detail_ruche, name = 'detail_ruche'),
    path('login',views.login, name = 'login'),
    path('ajout_cheptel',views.ajout_cheptel, name = 'ajout_cheptel'),
    path('ajout_intervention',views.ajout_intervention, name = 'ajout_intervention'),
    path('ajout_ruche',views.ajout_ruche, name = 'ajout_ruche'),
]