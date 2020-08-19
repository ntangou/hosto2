from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Titre, Personnel

# Create your views here.
def index(request):
    requete = Service.objects.all()
    return render(request, 'service/service.html', {'services':requete})

def personnel(request):
    requete = Personnel.objects.select_related('service')
    return render(request, 'service/personnel.html', {'personnels':requete})