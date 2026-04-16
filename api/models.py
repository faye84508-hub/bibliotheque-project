from django.db import models
from django.contrib.auth.models import User

# MODELE AUTEUR
class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    biographie = models.TextField(blank=True, null=True)
    nationalite = models.CharField(max_length=100, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


# MODELE TAG
class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


# MODELE LIVRE
class Livre(models.Model):
    CATEGORIES = [
        ('roman', 'Roman'),
        ('essai', 'Essai'),
        ('poesie', 'Poésie'),
        ('bd', 'Bande dessinée'),
        ('science', 'Science'),
        ('histoire', 'Histoire'),
    ]

    titre = models.CharField(max_length=300)
    isbn = models.CharField(max_length=17, unique=True)
    annee_publication = models.IntegerField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='roman')

    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')

    # 🔥 AJOUTS IMPORTANTS
    cree_par = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='livres')

    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
from django.contrib.auth.models import User

class ProfilLecteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_naissance = models.DateField(null=True, blank=True)

    # 🔥 Favoris
    livres_favoris = models.ManyToManyField(Livre, blank=True)

    def __str__(self):
        return self.user.username