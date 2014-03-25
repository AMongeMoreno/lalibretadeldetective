'''
Created on Mar 14, 2014

@author: Andres
'''
from django.db import models
from django.db.models.base import Model

class Tarea1(Model):
    alumno = models.CharField(max_length=15, blank = True, null = True, default="-")
     
    t1a_1 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_2 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_3 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_4 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_5 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_6 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_7 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_8 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_9 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_10 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_11 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_12 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_13 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_14 = models.CharField(max_length=1, blank = True, null = True, default="-")
    t1a_15 = models.CharField(max_length=1, blank = True, null = True, default="-")
    
    t1b_1_1 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_1_2 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_1_3 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_1_4 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_1_5 = models.CharField(max_length=15, blank = True, null = True, default="")
    
    t1b_2_1 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_2_2 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_2_3 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_2_4 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_2_5 = models.CharField(max_length=15, blank = True, null = True, default="")
    
    t1b_3_1 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_3_2 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_3_3 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_3_4 = models.CharField(max_length=15, blank = True, null = True, default="")
    t1b_3_5 = models.CharField(max_length=15, blank = True, null = True, default="")