import re
from random import choices
from sre_parse import CATEGORIES
from django import forms
from attr import fields
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm, NumberInput, TextInput
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import HiddenInput
from .models import *

# HOME PAGE
def index(request):

    banners = Banner.objects.all()
    horses = Horse.objects.all()
    peoples = People.objects.all()
    publications = Publication.objects.all()

    horses = horses.order_by('name')[:6]

    return render(request, "donate/index.html", {
        "banners": Banner.objects.all(),
        "horses": horses,
        "peoples": People.objects.all(),
        "publications": Publication.objects.all(),
    })

# DISPLAY SELECTED PUBLICATION
def publication(request, publication_id):
    pub = Publication.objects.get(pk=publication_id)
    publications = Publication.objects.exclude(pk=publication_id)
    return render(request, "donate/publication.html", {
        "pub": pub,
        "publications": publications,
    })

# DISPLAY HORSES
def horse(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    horses = Horse.objects.exclude(pk=horse_id)
    all_horses = horses.order_by('name')

    return render(request, "donate/horse.html", {
        "horses": all_horses,
        "horse": horse,
    })

def gallery(request):
    horses = Horse.objects.all()
    return render(request, "donate/gallery.html", {
        "horses": horses,
    })