#définition de la mise en page (forms) des html
from django import forms
from .models import Ruche,Cheptel, Intervention
from django.contrib.auth.decorators import login_required

class SomeForm(forms.Form):
    username = forms.CharField(label = "Nom utilisateur :")
    password = forms.CharField(label = "Mot de passe :", widget = forms.PasswordInput)

class AjoutCheptel(forms.ModelForm):
    
    class Meta:
        model = Cheptel
        fields = ['name']
        labels = {'name':'Nom'}

class AjoutRuche(forms.ModelForm):
        
    class Meta:
        model = Ruche
        fields = ['name','cheptel','status_hive','queen_birthday','type_bee','contamination']
        labels = {'name':'Nom','cheptel':'Cheptel','status_hive' : 'Statut de la ruche','queen_birthday':'Date naissance de la reine','type_bee':"Type d'abeille",'contamination':'Contamination'}
    
    #fonction pour alerter si l'âge de la reine est trop important. Juste pour l'exemple. Attention pour l'instant on n'a que la date de naissance de la reine et pas son age    
    def clean_taille(self):
        age = self.cleaned_data['queen_birthday']
        if age>80:
            raise forms.ValidationError("Attention l'age de la reine semble trop important")
        return age

class AjoutIntervention(forms.ModelForm):
    
    class Meta:
        model = Intervention
        fields = ['date','type_action','hive']
        labels = {'date':'Date','type_action':"Type d'action",'hive' : 'Ruche'}