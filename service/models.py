from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Service(models.Model):
    image_service = models.ImageField()
    nom_service = models.CharField(primary_key=True, max_length=50)
    specialisteM = models.CharField(unique=True, max_length=50)
    specialisteF = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.nom_service

class Titre(models.Model):
    titre = models.CharField(primary_key=True, max_length=50)
    
    
    def __str__(self):
        return self.titre


class Personnel(models.Model):
    choix_sexe = (
        ('M','M'),
        ('F', 'F'),
    )
    photo_personnel = models.ImageField(upload_to='imgdefaut/')
    nom_personnel = models.CharField(max_length=150)
    prenom_personnel = models.CharField(max_length=150, blank=True)
    sexe = models.CharField(max_length=50, choices = choix_sexe)
    titre = models.ForeignKey('Titre', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)


