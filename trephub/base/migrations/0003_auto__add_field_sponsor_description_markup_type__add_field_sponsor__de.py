# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sponsor.description_markup_type'
        db.add_column('base_sponsor', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30),
                      keep_default=False)

        # Adding field 'Sponsor._description_rendered'
        db.add_column('base_sponsor', '_description_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Sponsor.description'
        db.alter_column('base_sponsor', 'description', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

    def backwards(self, orm):
        # Deleting field 'Sponsor.description_markup_type'
        db.delete_column('base_sponsor', 'description_markup_type')

        # Deleting field 'Sponsor._description_rendered'
        db.delete_column('base_sponsor', '_description_rendered')


        # Changing field 'Sponsor.description'
        db.alter_column('base_sponsor', 'description', self.gf('django.db.models.fields.TextField')())

    models = {
        'base.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['base']