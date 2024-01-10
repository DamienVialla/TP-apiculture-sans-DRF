#model permettant de définir les tables dans la base de données
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

class Cheptel(models.Model):
    owner = models.CharField(max_length=40, null=False) #foreignkey, pas assez naturel dans son utilisation pour moi, je démultiplie donc l'attribut owner dans chaque classe. Je le force dans les views et donc pas de risque d'erreur
    name = models.CharField(max_length=40, null=False)
       
    #permet de changer la syntaxe apparente dans le menu admin
    class Meta:
        verbose_name = "Cheptel"
        verbose_name_plural = "Cheptels"
    
    #permet l'affichage des données et pas l'objet    
    def __str__(self):
        return self.name
    
class Ruche(models.Model):
    
    owner = models.CharField(max_length=40, null=False) #idem
    name = models.CharField(max_length=40, null=False) 
    cheptel = models.ForeignKey('Cheptel', on_delete=models.CASCADE) #clé étrangère pour relier le cheptel aux ruches
    choice_status_hive = (('En activité','En activité'),('En attente','En attente'),('Détruite','Détruite'))
    status_hive = models.CharField(choices = choice_status_hive,null=False)
    queen_birthday = models.DateField()
    choice_type_bee = (('A.Scutellata','A.Scutellata'),('A.Adansonii','A.Adansonii'),('A.Mellifera','A.Mellifera'),('A.Ligustica','A.Ligustica'),('A.Syriaca','A.Syriaca'),('A.Carnica','A.Carnica'),('A.Intermissa','A.Intermissa'),('Autre','Autre')) #trouvé dans la litterature
    type_bee = models.CharField(choices = choice_type_bee,null=False)
    choice_type_contamination = (('acarapisose','acarapisose'),('loque_américaine','loque américaine'),('infestation_par_le petit_coléoptère_des_ruches','infestation par_le_petit_coléoptère_des_ruches'),("infestation_par_l’acarien_Tropilaelaps","infestation par l’acarien Tropilaelaps"),('varroose','varroose'),('aucune','Aucune'))#trouvé dans la litterature
    contamination = models.CharField(choices = choice_type_contamination,null=False)  
    
    class Meta:
        verbose_name = "Caractéristique d'une ruche"
        verbose_name_plural = "Caractéristiques d'une ruche"
    
    def __str__(self):
        return self.name
        
class Intervention(models.Model):
    owner = models.CharField(max_length=40, null=False, default = "CedricJ")
    date = models.DateField()# pour tracer la date des interventions
    choice_intervention = (('Suppression_cellules_royales','Suppression_cellules_royales'),('verification_santé','Vérification santé'),('Récolte','Récolte'),('Pose_hausses','Pose hausses'),('Destruction','Destruction'),('Traitement','Traitement'))# cahier des charges
    type_action = models.CharField(max_length=100, choices = choice_intervention,null=False)
    hive = models.ForeignKey('Ruche', on_delete=models.CASCADE,related_name="interventions")#Clé étrangère pour lier les ruches aux interventions
    class Meta:
        verbose_name = "Intervention"
        verbose_name_plural = "Interventions"

