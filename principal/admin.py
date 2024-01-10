# gestion de la vue admin
from django.contrib import admin
from .models import Ruche, Cheptel, Intervention

@admin.register(Cheptel)
class CheptelAdmin(admin.ModelAdmin):
    #mise en page des champs qui doivent apparaitre   
    list_display = ('owner','name',)
    #faire une recherche de mots dans un champs
    search_fields = ['name']
    #nombre de lignes par page
    list_per_page = 10

@admin.register(Ruche)
class RucheAdmin(admin.ModelAdmin):
    #permet d'arranger la vue dans admin en créant des catégories
    fieldsets = [
        ('Status',{'fields' : ['name']}),
        ('Abeilles',{'fields' : ['queen_birthday','type_bee','contamination']}),
    ]
    #mise en page des champs qui doivent apparaitre   
    list_display = ('queen_birthday',)
    #permet de filtrer sur un champs
    list_filter = ['name']
    #faire une recherche de mots dans un champs
    search_fields = ['type_contamination']
    #nombre de lignes par page
    list_per_page = 10

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    #mise en page des champs qui doivent apparaitre   
    list_display = ('type_action',)
    #permet de filtrer sur un champs
    list_filter = ['type_action']
    #faire une recherche de mots dans un champs
    search_fields = ['type_action']
    #nombre de lignes par page
    list_per_page = 10
