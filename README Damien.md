# Django projet API sur gestion de cheptels

# contexte du projet 
Mettre en pratique les cours que nous avons reçu sur Django (framework conçu pour simplifier le processus de développement d'applications) :
1e partie => Django modèle MVT mise en place d'une architecture projet/app
2e partie => Django en tant qu'API reste

# présentation du rendu
le projet (APICULTUREPROJECT) comporte 3 app :
1- 'accounts' et 'principal' qui gère django comme framework permettant la gestion en templating de l'application.

Lors de la connexion au localhost, vous tomberez sur la page d'accueil qui vous permettra d'interagir avec la base de données. Avant toute chose, il faudra s'authentifier via un compte existant ou en crée un. Suite à cela vous pourrez créer des cheptels (ensemble de ruches), des ruches et implémenter des actions sur ces ruches. Vous aurez une vue sur l'ensemble des informations que vous avez rentré et des indicateurs sur vous interventions.

2- 'principalDRF' qui permet de travailler sur le format Json permettant par la suite au framework Angular de pouvoir utiliser les informations côté front.

Malheureusement, très peu de choses maitrisées ont été faites dans cette partie : (visualisables sur http://127.0.0.1:8000/DRF/)
a- la visualisation des différents chepets => "http://127.0.0.1:8000/DRF/cheptelDRFRUser/"
b- la vision des ruches seulement avec les "fields" présents dans le modèle. Par exemple, la notion de date de destruction, les quantités de récoltes et les dates de contaminations ne sont pas tracés car appartiennent à une autre table et impossible pour moi de faire le 'lien'. Seule chose rajoutée, c'est l'age en fonction de la date => http://127.0.0.1:8000/DRF/ruchesDRF/
c- la liste des interventions => http://127.0.0.1:8000/DRF/interventionsDRF/
d- des filtres sont disponibles sur la viewset de la Ruche
e- une action sur toutes les ruches du propriétaire avec changement de nom sur l'adresse suivante => "http://127.0.0.1:8000/DRF/changementglobal/" 

Attention, je n'ai pas réussi à faire de serialiseur "nested" car à chaque fois des problèmes de référence circulaire. Donc, beaucoup d'information avec l'id et pas le nom de l'attribut

## Démarrage de l'application
1. Créer un dossier sur votre ordinateur et l'ouvrir avec VSCode
2. Créer votre environnement virtuel avec la ligne de commande dans le terminal : `python -m venv <environment name>` (conseil, nommer l'environnement "venv")
3. Se Connecter à votre enrionnement en tappant dans le terminal : `.\<environment name>\Scripts\activate`
4. Cloner le repository du projet : `git clone https://github.com/DamienVialla/TP-apiculture.git`
5. Lancer les installation des applications nécessaires avec la ligne de commande dans le terminal : `pip install -r requirements.txt`. Attention, bien vérifier que vous êtes dans le dossier du projet, vaut également pour les autres lignes de commande (gestion de l'arborescence avec "cd")
6. Créer une base de données dans votre éditeur (ce projet a été fait avec postgres pour information)
7. Remplire le fichier .env-template avec vos information et le renommer en ".env"
8. Créer des tables dans votre base de données en fonction des modèles définis :`python manage.py migrate`
9. Créer un "admin" : `python manage.py createsuperuser`
10. Lancer l'application : `python manage.py runserver`
