#différentes fonctions relatives aux vues

from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST': #test si on est en ecriture
        username = request.POST["username"] #rentre le nom d'utilisateur
        password = request.POST["password"] #rentre le mot de passe
        
        user = authenticate(request, username = username, password = password) #enregistrement de l'utilsateur avec fonctionnalité native de django
        
        if user is not None: #si user ok
            login(request,user) #enregistrement
            return redirect('principal:index') #renvoie page accueil
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect") #message d'alerte
    
    form = AuthenticationForm() #on instancie le formulaire
    return render(request,"./login.html",{"form":form}) #on va sur la page login avec le formulaire

def logout_user(request):
    logout(request) #déconnection native
    return redirect ('principal:index') #renvoie page accueil

def register_user(request): #idem précédemment en enregistrement de user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:index')
    else :
        form = UserCreationForm()
    return render(request, "./register.html", {"form":form} )

