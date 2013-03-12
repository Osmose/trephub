# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sponsor.slug'
        db.add_column('base_sponsor', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', unique=True, max_length=50),
                      keep_default=False)

        # Adding unique constraint on 'Sponsor', fields ['name']
        db.create_unique('base_sponsor', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Sponsor', fields ['name']
        db.delete_unique('base_sponsor', ['name'])

        # Deleting field 'Sponsor.slug'
        db.delete_column('base_sponsor', 'slug')


    models = {
        'base.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['base']