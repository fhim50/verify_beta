# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Drug'
        db.create_table('verify_drug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.TextField')(max_length=300, db_index=True)),
            ('Generic_name', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('strength', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('dosage_form', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('applicant', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('local_agent', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.TextField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('verify', ['Drug'])

        # Adding model 'Food_water'
        db.create_table('verify_food_water', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.TextField')(max_length=500, db_index=True)),
            ('FDB_number', self.gf('django.db.models.fields.TextField')(max_length=15, blank=True)),
            ('manu_location', self.gf('django.db.models.fields.TextField')(max_length=300, blank=True)),
            ('dosage_form', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('verify', ['Food_water'])


    def backwards(self, orm):
        # Deleting model 'Drug'
        db.delete_table('verify_drug')

        # Deleting model 'Food_water'
        db.delete_table('verify_food_water')


    models = {
        'verify.drug': {
            'Generic_name': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'Meta': {'object_name': 'Drug'},
            'applicant': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'dosage_form': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.TextField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_agent': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.TextField', [], {'max_length': '300', 'db_index': 'True'}),
            'strength': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'})
        },
        'verify.food_water': {
            'FDB_number': ('django.db.models.fields.TextField', [], {'max_length': '15', 'blank': 'True'}),
            'Meta': {'object_name': 'Food_water'},
            'dosage_form': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manu_location': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.TextField', [], {'max_length': '500', 'db_index': 'True'})
        }
    }

    complete_apps = ['verify']