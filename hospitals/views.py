from django.shortcuts import render, redirect
from .models import Doctor, Patient

# Create your views here.
def index(request):
    return render(request, 'hospitals/index.html')