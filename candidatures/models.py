from django.db import models

# Create your models here.

class Candidature(models.Model):
    STATUT_CHOICES = [
        ('envoyee', 'Envoyée'),
        ('relancee', 'Relanée'),
        ('entretien', 'Entretien programé'),
        ('refusee', 'Refusée'),
        ('acceptée', 'Acceptée'),
    ]

    TYPE_CONTRAT = [
        ('alternance', 'Alternance'),
        ('stage', 'Stage'),
        ('non_precise', 'Non précisé')
    ]

    entreprise = models.CharField(max_length=100)
    poste = models.CharField(max_length=150)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT, default='non_precise')
    lien_annonce = models.URLField(blank=True, null=True)
    date_envoie = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='envoyee')
    note = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poste} chez {self.entreprise}"