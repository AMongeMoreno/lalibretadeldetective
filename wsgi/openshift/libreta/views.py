# Create your views here.
from django.shortcuts import render
def index(request):
    context = {}
    return render(request, 'libreta\index.html', context)