from django.db import models

# Create your models here.
class Engin(models.Model):
    categorie = models.CharField(max_length=255, default="")
    nom = models.CharField(max_length=255, default="")
    description = models.TextField(default="")

    def __unicode__(self):
        return "%s" % (self.description)

class Piece(models.Model):
    description = models.TextField(default="")
    nom = models.CharField(max_length=255, default="")
    numero = models.CharField(max_length=255, default="")
    PIECE_ETAT = (
            ('U', 'Used'),
            ('N', 'Neuf'),
    )
    etat = models.CharField(max_length=1, choices=PIECE_ETAT,  default='U')
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __unicode__(self):
        return "%s [%s]" % (self.description, self.numero)

class Outil(models.Model):
    nom = models.CharField(max_length=255, default="")
    numero = models.CharField(max_length=255, default="")
    description = models.TextField(default="")

    def __unicode__(self):
        return "%s, %s [%s]" % (self.type, self.description, self.numero)

class Client(models.Model):
    pass
