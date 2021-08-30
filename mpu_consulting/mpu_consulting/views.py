from typing import Dict
from django.http import JsonResponse, request, HttpResponse
import json
from django.template.loader import render_to_string
from .models import PortfolioEntry
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ClientForm


def index(request):
    form = ClientForm()
    if request.POST:
        fname = request.POST["fname"]
        email = request.POST["email"]
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'fname': fname, "email": email}
            email_notification(request, context)
            thank(request)
    context = {'form' :form}
    return render(request, "Home.html", context)


def thank(request):
    name_des_clienten = request.POST["fname"]
    name_des_clienten2 = {"name_des_clienten": name_des_clienten}
    return render(request, "Thank.html", name_des_clienten2)


def preise(request):
    form = ClientForm()
    if request.POST:
        print(request.POST)
        fname = request.POST["fname"]
        email = request.POST["email"]
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'fname': fname, "email": email}
            email_notification(request, context)
            thank(request)
    context = {'form': form}
    return render(request, "Preise.html", context)

def berater(request):
    form = ClientForm()
    if request.POST:
        print(request.POST)
        fname = request.POST["fname"]
        email = request.POST["email"]
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'fname': fname, "email": email}
            email_notification(request, context)
    context = {'form': form}
    return render(request, "Der_Berater.html", context)


def bertung(request):
    form = ClientForm()
    if request.POST:
        print(request.POST)
        fname = request.POST["fname"]
        email = request.POST["email"]
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'fname': fname, "email": email}
            email_notification(request, context)
    context = {'form': form}
    return render(request, "Die_Beratung.html", context)



def Impressum(request):

    return render(request, "Impressum.html")


def Datenschutz(request):
    return render(request, "Datenschutz.html")


def AGB(request):
    return render(request, "AGB.html")

def Widerrufsbelehrung(request):
    return render(request, "Widerrufsbelehrung.html")


def process_inquirey(request):
    form = ClientForm(request.POST)
    print(form)
    if form.is_valid():
        fname = form.clean_data['post']
    return render(request,  "Thank.html", {'form': form})


def email_notification(request, context):
    template = render_to_string('email_template.html', context)
    email = EmailMessage(
        'Neuer Client',
        template,
        settings.EMAIL_HOST_USER,
        ['Bretschneider.mpu@gmail.com'],
    )
    email.fail_silently = False
    email.send()