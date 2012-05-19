# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Engin'
        db.create_table('garage_engin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('garage', ['Engin'])

        # Adding model 'Piece'
        db.create_table('garage_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('garage', ['Piece'])

        # Adding model 'Outil'
        db.create_table('garage_outil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('garage', ['Outil'])

        # Adding model 'Client'
        db.create_table('garage_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('garage', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Engin'
        db.delete_table('garage_engin')

        # Deleting model 'Piece'
        db.delete_table('garage_piece')

        # Deleting model 'Outil'
        db.delete_table('garage_outil')

        # Deleting model 'Client'
        db.delete_table('garage_client')


    models = {
        'garage.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.engin': {
            'Meta': {'object_name': 'Engin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.outil': {
            'Meta': {'object_name': 'Outil'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'garage.piece': {
            'Meta': {'object_name': 'Piece'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['garage']