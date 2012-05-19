# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Engin.nom'
        db.add_column('garage_engin', 'nom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


        # Changing field 'Engin.categorie'
        db.alter_column('garage_engin', 'categorie', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Engin.description'
        db.alter_column('garage_engin', 'description', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Outil.type'
        db.delete_column('garage_outil', 'type')

        # Adding field 'Outil.nom'
        db.add_column('garage_outil', 'nom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


        # Changing field 'Outil.numero'
        db.alter_column('garage_outil', 'numero', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Outil.description'
        db.alter_column('garage_outil', 'description', self.gf('django.db.models.fields.TextField')())
        # Adding field 'Piece.nom'
        db.add_column('garage_piece', 'nom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Piece.prix'
        db.add_column('garage_piece', 'prix',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)


        # Changing field 'Piece.description'
        db.alter_column('garage_piece', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Piece.numero'
        db.alter_column('garage_piece', 'numero', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'Engin.nom'
        db.delete_column('garage_engin', 'nom')


        # Changing field 'Engin.categorie'
        db.alter_column('garage_engin', 'categorie', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Engin.description'
        db.alter_column('garage_engin', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding field 'Outil.type'
        db.add_column('garage_outil', 'type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Deleting field 'Outil.nom'
        db.delete_column('garage_outil', 'nom')


        # Changing field 'Outil.numero'
        db.alter_column('garage_outil', 'numero', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Outil.description'
        db.alter_column('garage_outil', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Deleting field 'Piece.nom'
        db.delete_column('garage_piece', 'nom')

        # Deleting field 'Piece.prix'
        db.delete_column('garage_piece', 'prix')


        # Changing field 'Piece.description'
        db.alter_column('garage_piece', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Piece.numero'
        db.alter_column('garage_piece', 'numero', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        'garage.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.engin': {
            'Meta': {'object_name': 'Engin'},
            'categorie': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'garage.outil': {
            'Meta': {'object_name': 'Outil'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'garage.piece': {
            'Meta': {'object_name': 'Piece'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'etat': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'prix': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['garage']