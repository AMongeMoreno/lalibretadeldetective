# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tarea1'
        db.create_table('LaLibretaDelDetective_tarea1', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1a_1', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_2', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_3', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_4', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_5', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_6', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_7', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_8', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_9', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_10', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_11', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_12', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_13', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_14', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1a_15', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=1)),
            ('t1b_1_1', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_1_2', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_1_3', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_1_4', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_1_5', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_2_1', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_2_2', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_2_3', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_2_4', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_2_5', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_3_1', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_3_2', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_3_3', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_3_4', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
            ('t1b_3_5', self.gf('django.db.models.fields.CharField')(blank=True, null=True, default='-', max_length=15)),
        ))
        db.send_create_signal('LaLibretaDelDetective', ['Tarea1'])


    def backwards(self, orm):
        # Deleting model 'Tarea1'
        db.delete_table('LaLibretaDelDetective_tarea1')


    models = {
        'LaLibretaDelDetective.tarea1': {
            'Meta': {'object_name': 'Tarea1'},
            'alumno': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't1a_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_11': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_12': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_13': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_14': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_15': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1a_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '1'}),
            't1b_1_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_1_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_1_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_1_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_1_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_2_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_2_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_2_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_2_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_2_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_3_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_3_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_3_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_3_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'}),
            't1b_3_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "'-'", 'max_length': '15'})
        }
    }

    complete_apps = ['LaLibretaDelDetective']