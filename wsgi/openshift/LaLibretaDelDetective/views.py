# Create your views here.
from LaLibretaDelDetective.models import Tarea1
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
        answer = Tarea1.objects.get(alumno=name)
        tarea1 = answer
        
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
#    if nombre is None:
#        return redirect('/')
    
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
        answer = Tarea1.objects.get(alumno=nombre)
        answer.t1a_1 = t1a_1 
        answer.t1a_2 = t1a_2 
        answer.t1a_3 = t1a_3 
        answer.t1a_4 = t1a_4 
        answer.t1a_5 = t1a_5 
        answer.t1a_6 = t1a_6 
        answer.t1a_7 = t1a_7 
        answer.t1a_8 = t1a_8 
        answer.t1a_9 = t1a_9 
        answer.t1a_10 = t1a_10 
        answer.t1a_11 = t1a_11 
        answer.t1a_12 = t1a_12 
        answer.t1a_13 = t1a_13 
        answer.t1a_14 = t1a_14 
        answer.t1a_15 = t1a_15 

        answer.t1b_1_1 = t1b_1_1
        answer.t1b_1_2 = t1b_1_2
        answer.t1b_1_3 = t1b_1_3
        answer.t1b_1_4 = t1b_1_4
        answer.t1b_1_5 = t1b_1_5

        answer.t1b_2_1 = t1b_2_1
        answer.t1b_2_2 = t1b_2_2
        answer.t1b_2_3 = t1b_2_3
        answer.t1b_2_4 = t1b_2_4
        answer.t1b_2_5 = t1b_2_5

        answer.t1b_3_1 = t1b_3_1
        answer.t1b_3_2 = t1b_3_2
        answer.t1b_3_3 = t1b_3_3
        answer.t1b_3_4 = t1b_3_4
        answer.t1b_3_5 = t1b_3_5

    except Tarea1.DoesNotExist:
        answer = Tarea1(alumno=nombre, t1a_1=t1a_1, t1a_2=t1a_2, t1a_3=t1a_3, t1a_4=t1a_4, t1a_5=t1a_5,
                        t1a_6=t1a_6, t1a_7=t1a_7, t1a_8=t1a_8, t1a_9=t1a_9, t1a_10=t1a_10, t1a_11=t1a_11,
                        t1a_12=t1a_12, t1a_13=t1a_13, t1a_14=t1a_14, t1a_15=t1a_15, 
                        t1b_1_1=t1b_1_1, t1b_1_2=t1b_1_2, t1b_1_3=t1b_1_3, t1b_1_4=t1b_1_4, t1b_1_5=t1b_1_5,
                        t1b_2_1=t1b_2_1, t1b_2_2=t1b_2_2, t1b_2_3=t1b_2_3, t1b_2_4=t1b_2_4, t1b_2_5=t1b_2_5,
                        t1b_3_1=t1b_3_1, t1b_3_2=t1b_3_2, t1b_3_3=t1b_3_3, t1b_3_4=t1b_3_4, t1b_3_5=t1b_3_5)
    
    answer.save()
        
    # Tarea 2
    # Tarea 3
    # Tarea 4
    # Tarea 5
    # Tarea 6
    result = 'success';
    return HttpResponse("{'result':'" + result + "'}");
    
