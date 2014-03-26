# Create your views here.
from LaLibretaDelDetective.models import Tarea1, Tarea2, Tarea3, Tarea5, Tarea6
from django.core.files.base import File
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import settings
@ensure_csrf_cookie
def index(request):
    context = {}
    return render(request, 'LaLibretaDelDetective/index.html', context)

@ensure_csrf_cookie
def libreta(request):
    name = request.GET.get('input-name')
    if (name is None):
        return redirect('/')
    try: 
        tarea1 = Tarea1.objects.get(alumno=name)
        tarea1 = tarea1
        
    except Tarea1.DoesNotExist:
        tarea1 = {'t1a_1' : '-','t1a_2' : '-','t1a_3' : '-','t1a_4' : '-',
                   't1a_5' : '-','t1a_6' : '-','t1a_7' : '-','t1a_8' : '-',
                   't1a_9' : '-','t1a_10' : '-','t1a_11' : '-','t1a_12' : '-',
                   't1a_13' : '-','t1a_14' : '-','t1a_15' : '-'}
    
    context = {'nombre' : name, 'tarea1':  tarea1}
    return render(request, 'LaLibretaDelDetective/libreta.html', context)

@ensure_csrf_cookie
def libreta_save(request):
    nombre = request.POST.get('nombre')
    if nombre is None:
        return redirect('/')
    
    # Tarea 1
    t1a_1 = request.POST.get('input-t1a-1')
    t1a_2 = request.POST.get('input-t1a-2')
    t1a_3 = request.POST.get('input-t1a-3')
    t1a_4 = request.POST.get('input-t1a-4')
    t1a_5 = request.POST.get('input-t1a-5')
    t1a_6 = request.POST.get('input-t1a-6')
    t1a_7 = request.POST.get('input-t1a-7')
    t1a_8 = request.POST.get('input-t1a-8')
    t1a_9 = request.POST.get('input-t1a-9')
    t1a_10 = request.POST.get('input-t1a-10')
    t1a_11 = request.POST.get('input-t1a-11')
    t1a_12 = request.POST.get('input-t1a-12')
    t1a_13 = request.POST.get('input-t1a-13')
    t1a_14 = request.POST.get('input-t1a-14')
    t1a_15 = request.POST.get('input-t1a-15')
    
    t1b_1_1 = request.POST.get('input-t1b-1-1')
    t1b_1_2 = request.POST.get('input-t1b-1-2')
    t1b_1_3 = request.POST.get('input-t1b-1-3')
    t1b_1_4 = request.POST.get('input-t1b-1-4')
    t1b_1_5 = request.POST.get('input-t1b-1-5')
    
    t1b_2_1 = request.POST.get('input-t1b-2-1')
    t1b_2_2 = request.POST.get('input-t1b-2-2')
    t1b_2_3 = request.POST.get('input-t1b-2-3')
    t1b_2_4 = request.POST.get('input-t1b-2-4')
    t1b_2_5 = request.POST.get('input-t1b-2-5')
    
    t1b_3_1 = request.POST.get('input-t1b-3-1')
    t1b_3_2 = request.POST.get('input-t1b-3-2')
    t1b_3_3 = request.POST.get('input-t1b-3-3')
    t1b_3_4 = request.POST.get('input-t1b-3-4')
    t1b_3_5 = request.POST.get('input-t1b-3-5')
    try: 
        tarea1 = Tarea1.objects.get(alumno=nombre)
        tarea1.t1a_1 = t1a_1 
        tarea1.t1a_2 = t1a_2 
        tarea1.t1a_3 = t1a_3 
        tarea1.t1a_4 = t1a_4 
        tarea1.t1a_5 = t1a_5 
        tarea1.t1a_6 = t1a_6 
        tarea1.t1a_7 = t1a_7 
        tarea1.t1a_8 = t1a_8 
        tarea1.t1a_9 = t1a_9 
        tarea1.t1a_10 = t1a_10 
        tarea1.t1a_11 = t1a_11 
        tarea1.t1a_12 = t1a_12 
        tarea1.t1a_13 = t1a_13 
        tarea1.t1a_14 = t1a_14 
        tarea1.t1a_15 = t1a_15 

        tarea1.t1b_1_1 = t1b_1_1
        tarea1.t1b_1_2 = t1b_1_2
        tarea1.t1b_1_3 = t1b_1_3
        tarea1.t1b_1_4 = t1b_1_4
        tarea1.t1b_1_5 = t1b_1_5

        tarea1.t1b_2_1 = t1b_2_1
        tarea1.t1b_2_2 = t1b_2_2
        tarea1.t1b_2_3 = t1b_2_3
        tarea1.t1b_2_4 = t1b_2_4
        tarea1.t1b_2_5 = t1b_2_5

        tarea1.t1b_3_1 = t1b_3_1
        tarea1.t1b_3_2 = t1b_3_2
        tarea1.t1b_3_3 = t1b_3_3
        tarea1.t1b_3_4 = t1b_3_4
        tarea1.t1b_3_5 = t1b_3_5

    except Tarea1.DoesNotExist:
        tarea1 = Tarea1(alumno=nombre, t1a_1=t1a_1, t1a_2=t1a_2, t1a_3=t1a_3, t1a_4=t1a_4, t1a_5=t1a_5,
                        t1a_6=t1a_6, t1a_7=t1a_7, t1a_8=t1a_8, t1a_9=t1a_9, t1a_10=t1a_10, t1a_11=t1a_11,
                        t1a_12=t1a_12, t1a_13=t1a_13, t1a_14=t1a_14, t1a_15=t1a_15, 
                        t1b_1_1=t1b_1_1, t1b_1_2=t1b_1_2, t1b_1_3=t1b_1_3, t1b_1_4=t1b_1_4, t1b_1_5=t1b_1_5,
                        t1b_2_1=t1b_2_1, t1b_2_2=t1b_2_2, t1b_2_3=t1b_2_3, t1b_2_4=t1b_2_4, t1b_2_5=t1b_2_5,
                        t1b_3_1=t1b_3_1, t1b_3_2=t1b_3_2, t1b_3_3=t1b_3_3, t1b_3_4=t1b_3_4, t1b_3_5=t1b_3_5)
    
    tarea1.save()
        
    # Tarea 2
    t2_1 = request.POST.get('t2_1')
    t2_2 = request.POST.get('t2_2')
    t2_3 = request.POST.get('t2_3')
    t2_4 = request.POST.get('t2_4')
    t2_5 = request.POST.get('t2_5')
    t2_6 = request.POST.get('t2_6')
    t2_7 = request.POST.get('t2_7')
    t2_8 = request.POST.get('t2_8')
    t2_9 = request.POST.get('t2_9')
    t2_10 = request.POST.get('t2_10')
    
    try: 
        tarea2 = Tarea2.objects.get(alumno=nombre)
        tarea2.t2_1 = t2_1 
        tarea2.t2_2 = t2_2 
        tarea2.t2_3 = t2_3 
        tarea2.t2_4 = t2_4 
        tarea2.t2_5 = t2_5 
        tarea2.t2_6 = t2_6 
        tarea2.t2_7 = t2_7 
        tarea2.t2_8 = t2_8 
        tarea2.t2_9 = t2_9 
        tarea2.t2_10 = t2_10 

    except Tarea2.DoesNotExist:
        tarea2 = Tarea2(alumno=nombre, 
		t2_1 = t2_1 ,
		t2_2 = t2_2 ,
		t2_3 = t2_3 ,
		t2_4 = t2_4 ,
		t2_5 = t2_5 ,
		t2_6 = t2_6 ,
		t2_7 = t2_7 ,
		t2_8 = t2_8 ,
		t2_9 = t2_9 ,
        t2_10 = t2_10)
        
    tarea2.save()
    
    # Tarea 3
    t3_1 = request.POST.get('t3_1')
    t3_2 = request.POST.get('t3_2')
    t3_3 = request.POST.get('t3_3')
    t3_4 = request.POST.get('t3_4')
    t3_5 = request.POST.get('t3_5')
    t3_6 = request.POST.get('t3_6')
    t3_7 = request.POST.get('t3_7')
    t3_8 = request.POST.get('t3_8')
    t3_9 = request.POST.get('t3_9')
    t3_10 = request.POST.get('t3_10')
    t3_11 = request.POST.get('t3_11')
    t3_12 = request.POST.get('t3_12')
    t3_13 = request.POST.get('t3_13')
    t3_14 = request.POST.get('t3_14')
    t3_15 = request.POST.get('t3_15')
    t3_16 = request.POST.get('t3_16')
    t3_17 = request.POST.get('t3_17')
    t3_18 = request.POST.get('t3_18')
    t3_19 = request.POST.get('t3_19')
    t3_20 = request.POST.get('t3_20')
    t3_21 = request.POST.get('t3_21')
    t3_22 = request.POST.get('t3_22')
    t3_23 = request.POST.get('t3_23')
    t3_24 = request.POST.get('t3_24')
    t3_25 = request.POST.get('t3_25')
    t3_26 = request.POST.get('t3_26')
    t3_27 = request.POST.get('t3_27')
    t3_28 = request.POST.get('t3_28')
    t3_29 = request.POST.get('t3_29')
    t3_30 = request.POST.get('t3_30')
    
    try: 
        tarea3 = Tarea3.objects.get(alumno=nombre)
        tarea3.t3_1 = t3_1 
        tarea3.t3_2 = t3_2 
        tarea3.t3_3 = t3_3 
        tarea3.t3_4 = t3_4 
        tarea3.t3_5 = t3_5 
        tarea3.t3_6 = t3_6 
        tarea3.t3_7 = t3_7 
        tarea3.t3_8 = t3_8 
        tarea3.t3_9 = t3_9 
        tarea3.t3_10 = t3_10 
        tarea3.t3_11 = t3_11 
        tarea3.t3_12 = t3_12 
        tarea3.t3_13 = t3_13 
        tarea3.t3_14 = t3_14 
        tarea3.t3_15 = t3_15 
        tarea3.t3_16 = t3_16 
        tarea3.t3_17 = t3_17 
        tarea3.t3_18 = t3_18 
        tarea3.t3_19 = t3_19 
        tarea3.t3_20 = t3_20 
        tarea3.t3_21 = t3_21 
        tarea3.t3_22 = t3_22 
        tarea3.t3_23 = t3_23 
        tarea3.t3_24 = t3_24 
        tarea3.t3_25 = t3_25 
        tarea3.t3_26 = t3_26 
        tarea3.t3_27 = t3_27 
        tarea3.t3_28 = t3_28 
        tarea3.t3_29 = t3_29 
        tarea3.t3_30 = t3_30 

    except Tarea3.DoesNotExist:
        tarea3 = Tarea3(alumno=nombre, 
		t3_1 = t3_1 ,
		t3_2 = t3_2 ,
		t3_3 = t3_3 ,
		t3_4 = t3_4 ,
		t3_5 = t3_5 ,
		t3_6 = t3_6 ,
		t3_7 = t3_7 ,
		t3_8 = t3_8 ,
		t3_9 = t3_9 ,
        t3_10 = t3_10 ,
        t3_11 = t3_11 ,
		t3_12 = t3_12 ,
		t3_13 = t3_13 ,
		t3_14 = t3_14 ,
		t3_15 = t3_15 ,
		t3_16 = t3_16 ,
		t3_17 = t3_17 ,
		t3_18 = t3_18 ,
		t3_19 = t3_19 ,
		t3_20 = t3_20 ,
		t3_21 = t3_21 ,
		t3_22 = t3_22 ,
		t3_23 = t3_23 ,
		t3_24 = t3_24 ,
		t3_25 = t3_25 ,
		t3_26 = t3_26 ,
		t3_27 = t3_27 ,
		t3_28 = t3_28 ,
		t3_29 = t3_29 ,
		t3_30 = t3_30 )

    tarea3.save()
    
    # Tarea 4
    

    # Tarea 5
    t5_1 = request.POST.get('t5_1')
    t5_2 = request.POST.get('t5_2')
    t5_3 = request.POST.get('t5_3')
    t5_4 = request.POST.get('t5_4')
    t5_5 = request.POST.get('t5_5')
    t5_6 = request.POST.get('t5_6')
    t5_7 = request.POST.get('t5_7')
    t5_8 = request.POST.get('t5_8')
    t5_9 = request.POST.get('t5_9')
    t5_10 = request.POST.get('t5_10')
    
    try: 
        tarea5 = Tarea5.objects.get(alumno=nombre)
        tarea5.t5_1 = t5_1 
        tarea5.t5_2 = t5_2 
        tarea5.t5_3 = t5_3 
        tarea5.t5_4 = t5_4 
        tarea5.t5_5 = t5_5 
        tarea5.t5_6 = t5_6 
        tarea5.t5_7 = t5_7 
        tarea5.t5_8 = t5_8 
        tarea5.t5_9 = t5_9 
        tarea5.t5_10 = t5_10 

    except Tarea5.DoesNotExist:
        tarea5 = Tarea5(alumno=nombre, 
		t5_1 = t5_1 ,
		t5_2 = t5_2 ,
		t5_3 = t5_3 ,
		t5_4 = t5_4 ,
		t5_5 = t5_5 ,
		t5_6 = t5_6 ,
		t5_7 = t5_7 ,
		t5_8 = t5_8 ,
		t5_9 = t5_9 ,
        t5_10 = t5_10)
        
    tarea5.save()
    
    # Tarea 6
    t6_1 = request.POST.get('t6_1')
    t6_2 = request.POST.get('t6_2')

    try: 
        tarea6 = Tarea6.objects.get(alumno=nombre)
        tarea6.t6_1 = t6_1 
        tarea6.t6_2 = t6_2 


    except Tarea6.DoesNotExist:
        tarea6 = Tarea6(alumno=nombre, 
		t6_1 = t6_1 ,
		t6_2 = t6_2 )
        
    tarea5.save()

    result = 'success';
    return HttpResponse("{'result':'" + result + "'}");
    
