from django.shortcuts import render, get_object_or_404,redirect
from .forms import SomeForm, AjoutRuche, AjoutCheptel, AjoutIntervention
from .models import Cheptel, Ruche, Intervention
from dateutil.relativedelta import relativedelta
from datetime import date

#ici qu'on gère les vues (MVT) en renvoyant les context dans le render à l'adresse url souhaitée

def PagePrincipale(request):
    #le context définit les "variables" que l'on souhaite mettre dans les html. Ici page principale
    context = {
        "cheptels": Cheptel.objects.all().filter(owner=request.user), #définit les cheptels de l'utilisateur connecté 
        "ruches": Ruche.objects.all().filter(owner=request.user), #idem avec les ruches
        "totaux" : Ruche.objects.all(), # toutes les ruches de tous les utilisateurs
        "interventions" : Intervention.objects.all().filter(owner=request.user), # intervention de l'utilisateur
        #ci-dessous les filtres pour les différentes interventions 
        "interventionsSuppression_cellules_royales" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='Suppression_cellules_royales'),
        "interventionsverification_sante" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='verification_santé'),
        "interventionsRecole" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='Récolte'),
        "interventionsPose_hausses" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='Pose_hausses'),
        "interventionsDestruction" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='Destruction'),
        "interventionsTraitement" : Intervention.objects.all().filter(owner=request.user).filter(type_action ='Traitement'),
        }
    return render(request, './index.html',context)
    
def login(request):
    if request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            return redirect("principal:index")
    else :
        form=SomeForm()
    
    context = {"form" : form}
    return render(request, './login.html', context)  

def ajout_cheptel(request):
    if request.method == 'POST':
        form = AjoutCheptel(request.POST)
        if form.is_valid():
            form.instance.owner = request.user #on force l'attribut owner avec le nom de la personne connectée
            form.save()
            return redirect("principal:index")
    else :
        form=AjoutCheptel()
    
    context = {
        "form" : form
        }
    return render(request, './ajout_cheptel.html', context)

def ajout_ruche(request):
    if request.method == 'POST':
        form = AjoutRuche(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect("principal:index")
    else :
        form=AjoutRuche()
    
    form.fields['cheptel'].queryset = Cheptel.objects.filter(owner=request.user) #on mets à jour le cheptel avec ceux de la personne connectée afin que dans le filtre n'apparaisse que ses cheptels
    
    context = {
        "form" : form
        }
    return render(request, './ajout_ruche.html', context)  

def ajout_intervention(request):
    if request.method == 'POST':
        form = AjoutIntervention(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect("principal:index")
    else :
        form=AjoutIntervention()
    
    form.fields['hive'].queryset = Ruche.objects.filter(owner=request.user)

    context = {
        "form" : form,
        }
    return render(request, './ajout_intervention.html', context) 

def detail_ruche(request, ruche_id):
    
    #transforme la date de naissance de la reine en age (mois)
    ruche = get_object_or_404(Ruche.objects.defer("queen_birthday"), pk=ruche_id)
    age = relativedelta(date.today(), ruche.queen_birthday).months
    
    context = {
        "ruches":get_object_or_404(Ruche, pk = ruche_id),
        "age":age
    }
    return render(request, './detail_ruche.html',context)

