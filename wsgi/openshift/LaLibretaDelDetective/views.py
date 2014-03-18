# Create your views here.
from django.shortcuts import render_to_response

def index(request): 
    context = {}
    return render_to_response(request, 'LaLibretaDelDetective/index.html', context)