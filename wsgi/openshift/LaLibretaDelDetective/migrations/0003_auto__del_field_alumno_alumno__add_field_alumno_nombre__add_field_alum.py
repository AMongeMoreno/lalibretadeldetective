# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Alumno.alumno'
        db.delete_column('LaLibretaDelDetective_alumno', 'alumno')

        # Adding field 'Alumno.nombre'
        db.add_column('LaLibretaDelDetective_alumno', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=25),
                      keep_default=False)

        # Adding field 'Alumno.apellidos'
        db.add_column('LaLibretaDelDetective_alumno', 'apellidos',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=50),
                      keep_default=False)

        # Adding field 'Alumno.username'
        db.add_column('LaLibretaDelDetective_alumno', 'username',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=20),
                      keep_default=False)

        # Adding field 'Alumno.password'
        db.add_column('LaLibretaDelDetective_alumno', 'password',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Alumno.alumno'
        db.add_column('LaLibretaDelDetective_alumno', 'alumno',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=50),
                      keep_default=False)

        # Deleting field 'Alumno.nombre'
        db.delete_column('LaLibretaDelDetective_alumno', 'nombre')

        # Deleting field 'Alumno.apellidos'
        db.delete_column('LaLibretaDelDetective_alumno', 'apellidos')

        # Deleting field 'Alumno.username'
        db.delete_column('LaLibretaDelDetective_alumno', 'username')

        # Deleting field 'Alumno.password'
        db.delete_column('LaLibretaDelDetective_alumno', 'password')


    models = {
        'LaLibretaDelDetective.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellidos': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '25'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '16'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '20'})
        },
        'LaLibretaDelDetective.tarea1': {
            'Meta': {'object_name': 'Tarea1'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't1a_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_11': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_12': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_13': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_14': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_15': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1a_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'-'", 'max_length': '1', 'null': 'True'}),
            't1b_1_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_1_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_1_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_1_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_1_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_2_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_2_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_2_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_2_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_2_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_3_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_3_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_3_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_3_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'}),
            't1b_3_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '15', 'null': 'True'})
        },
        'LaLibretaDelDetective.tarea2': {
            'Meta': {'object_name': 'Tarea2'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't2_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't2_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'})
        },
        'LaLibretaDelDetective.tarea3': {
            'Meta': {'object_name': 'Tarea3'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't3_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_11': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_12': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_13': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_14': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_15': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_16': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_17': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_18': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_19': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_20': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_21': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_22': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_23': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_24': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_25': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_26': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_27': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_28': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_29': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_30': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't3_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'})
        },
        'LaLibretaDelDetective.tarea4': {
            'Meta': {'object_name': 'Tarea4'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't4_10_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_10_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_10_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_10_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_10_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_1_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_1_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_1_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_1_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_2_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_2_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_2_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_2_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_3_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_3_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_3_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_3_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_4_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_4_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_4_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_4_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_5_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_5_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_5_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_5_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_6_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_6_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_6_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_6_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_7_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_7_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_7_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_7_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_8_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_8_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_8_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_8_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_9_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_9_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '300', 'null': 'True'}),
            't4_9_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'}),
            't4_9_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '30', 'null': 'True'})
        },
        'LaLibretaDelDetective.tarea5': {
            'Meta': {'object_name': 'Tarea5'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't5_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_10': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't5_9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'})
        },
        'LaLibretaDelDetective.tarea6': {
            'Meta': {'object_name': 'Tarea6'},
            'alumno': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            't6_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '800', 'null': 'True'}),
            't6_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '1200', 'null': 'True'})
        }
    }

    complete_apps = ['LaLibretaDelDetective']