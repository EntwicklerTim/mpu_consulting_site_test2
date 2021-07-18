from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'Key' : '<h4 class="margin">Anfrage:</h4>'}
    return render(request, "Home.html", my_dict)

def thank(request):
    #thank_dict = {'KEY':'Value'}
    name_des_clienten = request.GET["fname"]
    name_des_clienten2 = {"name_des_clienten": name_des_clienten}
    return render(request, "Thank.html", name_des_clienten2)
      #path('Thank', views.thank, name='Thank')

def preise(request):
    return render(request, "Preise.html")

def berater(request):
    return render(request, "Der_Berater.html")


def bertung(request):
    return render(request, "Die_Beratung.html")



def Impressum(request):
    return render(request, "Impressum.html")


def Datenschutz(request):
    return render(request, "Datenschutz.html")


def AGB(request):
    return render(request, "AGB.html")
