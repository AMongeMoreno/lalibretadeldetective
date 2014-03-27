'''
Created on Mar 14, 2014

@author: Andres
'''
from django.db import models
from django.db.models.base import Model

class Alumno(Model):
    nombre = models.CharField(max_length=25,default="NONE")
    apellidos = models.CharField(max_length=50,default="NONE")
    username = models.CharField(max_length=20,default="NONE")
    password = models.CharField(max_length=16,default="NONE")
    def __unicode__(self):  
        return self.nombre +','+ self.apellidos +','+ self.username +','+ self.password
    
    
class Tarea1(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
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
    
    def __unicode__(self):  
        return  self.alumno+','+self.t1a_1    +','+self.t1a_2    +','+self.t1a_3    +','+self.t1a_4    +','+self.t1a_5    +','+self.t1a_6    +','+self.t1a_7    +','+self.t1a_8    +','+self.t1a_9    +','+self.t1a_10   +','+self.t1a_11   +','+self.t1a_12   +','+self.t1a_13   +','+self.t1a_14   +','+self.t1a_15   +','+              self.t1b_1_1  +','+self.t1b_1_2  +','+self.t1b_1_3  +','+self.t1b_1_4  +','+self.t1b_1_5  +','+              self.t1b_2_1  +','+self.t1b_2_2  +','+self.t1b_2_3  +','+self.t1b_2_4  +','+self.t1b_2_5  +','+              self.t1b_3_1  +','+self.t1b_3_2  +','+self.t1b_3_3  +','+self.t1b_3_4  +','+self.t1b_3_5  

class Tarea2(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
    t2_1 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_2 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_3 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_7 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_8 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_9 = models.CharField(max_length=300, blank = True, null = True, default="")
    t2_10 = models.CharField(max_length=300, blank = True, null = True, default="")
    def __unicode__(self):
        return  self.alumno+','+self.t2_1 +','+self.t2_2 +','+self.t2_3 +','+self.t2_4 +','+self.t2_5 +','+self.t2_6 +','+self.t2_7 +','+self.t2_8 +','+self.t2_9 +','+self.t2_10

class Tarea3(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
    t3_1 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_2 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_3 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_7 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_8 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_9 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_10 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_11 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_12 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_13 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_14 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_15 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_16 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_17 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_18 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_19 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_20 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_21 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_22 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_23 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_24 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_25 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_26 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_27 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_28 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_29 = models.CharField(max_length=300, blank = True, null = True, default="")
    t3_30 = models.CharField(max_length=300, blank = True, null = True, default="")
    def __unicode__(self):
        return self.alumno+','+self.t3_1 +','+self.t3_2 +','+self.t3_3 +','+self.t3_4 +','+self.t3_5 +','+self.t3_6 +','+self.t3_7 +','+self.t3_8 +','+self.t3_9 +','+self.t3_10+','+self.t3_11+','+self.t3_12+','+self.t3_13+','+self.t3_14+','+self.t3_15+','+self.t3_16+','+self.t3_17+','+self.t3_18+','+self.t3_19+','+self.t3_20+','+self.t3_21+','+self.t3_22+','+self.t3_23+','+self.t3_24+','+self.t3_25+','+self.t3_26+','+self.t3_27+','+self.t3_28+','+self.t3_29+','+self.t3_30

class Tarea4(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
    t4_1_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_1_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_1_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_1_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_1_10 = models.CharField(max_length=30, blank = True, null = True, default="")

    t4_2_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_2_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_2_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_2_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_2_10 = models.CharField(max_length=30, blank = True, null = True, default="")
        
    t4_3_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_3_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_3_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_3_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_3_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_4_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_4_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_4_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_4_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_4_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_5_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_5_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_5_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_5_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_5_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_6_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_6_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_6_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_6_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_6_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_7_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_7_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_7_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_7_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_7_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_8_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_8_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_8_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_8_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_8_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_9_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_9_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_9_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_9_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_9_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    
    t4_10_1 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_2 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_3 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_4 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_10_5 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_10_6 = models.CharField(max_length=300, blank = True, null = True, default="")
    t4_10_7 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_8 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_9 = models.CharField(max_length=30, blank = True, null = True, default="")
    t4_10_10 = models.CharField(max_length=30, blank = True, null = True, default="")
    def __unicode__(self):
        return self.alumno+','+self.t4_1_1 +','+self.t4_1_2 +','+self.t4_1_3 +','+self.t4_1_4 +','+self.t4_1_5 +','+self.t4_1_6 +','+self.t4_1_7 +','+self.t4_1_8 +','+self.t4_1_9 +','+self.t4_1_10+','+self.t4_2_1 +','+self.t4_2_2 +','+self.t4_2_3 +','+self.t4_2_4 +','+self.t4_2_5 +','+self.t4_2_6 +','+self.t4_2_7 +','+self.t4_2_8 +','+self.t4_2_9 +','+self.t4_2_10+','+self.t4_3_1 +','+self.t4_3_2 +','+self.t4_3_3 +','+self.t4_3_4 +','+self.t4_3_5 +','+self.t4_3_6 +','+self.t4_3_7 +','+self.t4_3_8 +','+self.t4_3_9 +','+self.t4_3_10+','+self.t4_4_1 +','+self.t4_4_2 +','+self.t4_4_3 +','+self.t4_4_4 +','+self.t4_4_5 +','+self.t4_4_6 +','+self.t4_4_7 +','+self.t4_4_8 +','+self.t4_4_9 +','+self.t4_4_10+','+self.t4_5_1 +','+self.t4_5_2 +','+self.t4_5_3 +','+self.t4_5_4 +','+self.t4_5_5 +','+self.t4_5_6 +','+self.t4_5_7 +','+self.t4_5_8 +','+self.t4_5_9 +','+self.t4_5_10+','+self.t4_6_1 +','+self.t4_6_2 +','+self.t4_6_3 +','+self.t4_6_4 +','+self.t4_6_5 +','+self.t4_6_6 +','+self.t4_6_7 +','+self.t4_6_8 +','+self.t4_6_9 +','+self.t4_6_10+','+self.t4_7_1 +','+self.t4_7_2 +','+self.t4_7_3 +','+self.t4_7_4 +','+self.t4_7_5 +','+self.t4_7_6 +','+self.t4_7_7 +','+self.t4_7_8 +','+self.t4_7_9 +','+self.t4_7_10+','+self.t4_8_1 +','+self.t4_8_2 +','+self.t4_8_3 +','+self.t4_8_4 +','+self.t4_8_5 +','+self.t4_8_6 +','+self.t4_8_7 +','+self.t4_8_8 +','+self.t4_8_9 +','+self.t4_8_10+','+self.t4_9_1 +','+self.t4_9_2 +','+self.t4_9_3 +','+self.t4_9_4 +','+self.t4_9_5 +','+self.t4_9_6 +','+self.t4_9_7 +','+self.t4_9_8 +','+self.t4_9_9 +','+self.t4_9_10 +','+             self.t4_10_1 +','+self.t4_10_2 +','+self.t4_10_3 +','+self.t4_10_4 +','+self.t4_10_5 +','+self.t4_10_6 +','+self.t4_10_7 +','+self.t4_10_8 +','+self.t4_10_9 +','+self.t4_10_10

class Tarea5(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
    t5_1 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_2 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_3 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_4 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_5 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_6 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_7 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_8 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_9 = models.CharField(max_length=800, blank = True, null = True, default="")
    t5_10 = models.CharField(max_length=800, blank = True, null = True, default="")
    def __unicode__(self):
        return self.alumno+','+self.t5_1 +','+self.t5_2 +','+self.t5_3 +','+self.t5_4 +','+self.t5_5 +','+self.t5_6 +','+self.t5_7 +','+self.t5_8 +','+self.t5_9 +','+self.t5_10
    
class Tarea6(Model):
    alumno = models.CharField(max_length=50,default="NONE")
     
    t6_1 = models.CharField(max_length=800, blank = True, null = True, default="")
    t6_2 = models.CharField(max_length=1200, blank = True, null = True, default="")
    def __unicode__(self):
        return self.alumno+','+self.t6_1+','+self.t6_2