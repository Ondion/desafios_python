from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.


def index(request):
    return render(request, 'principal/index.html')