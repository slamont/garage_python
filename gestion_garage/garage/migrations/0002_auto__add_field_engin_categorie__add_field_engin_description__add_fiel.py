# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Engin.categorie'
        db.add_column('garage_engin', 'categorie',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Engin.description'
        db.add_column('garage_engin', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Outil.description'
        db.add_column('garage_outil', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Outil.numero'
        db.add_column('garage_outil', 'numero',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Outil.type'
        db.add_column('garage_outil', 'type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Piece.description'
        db.add_column('garage_piece', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Piece.numero'
        db.add_column('garage_piece', 'numero',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Piece.etat'
        db.add_column('garage_piece', 'etat',
                      self.gf('django.db.models.fields.CharField')(default='U', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Engin.categorie'
        db.delete_column('garage_engin', 'categorie')

        # Deleting field 'Engin.description'
        db.delete_column('garage_engin', 'description')

        # Deleting field 'Outil.description'
        db.delete_column('garage_outil', 'description')

        # Deleting field 'Outil.numero'
        db.delete_column('garage_outil', 'numero')

        # Deleting field 'Outil.type'
        db.delete_column('garage_outil', 'type')

        # Deleting field 'Piece.description'
        db.delete_column('garage_piece', 'description')

        # Deleting field 'Piece.numero'
        db.delete_column('garage_piece', 'numero')

        # Deleting field 'Piece.etat'
        db.delete_column('garage_piece', 'etat')


    models = {
        'garage.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.engin': {
            'Meta': {'object_name': 'Engin'},
            'categorie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.outil': {
            'Meta': {'object_name': 'Outil'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'garage.piece': {
            'Meta': {'object_name': 'Piece'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'etat': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['garage']