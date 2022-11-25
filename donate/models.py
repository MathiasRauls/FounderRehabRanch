import datetime
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

class Banner(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Banner Image Dimensions: 2000px X 700px', editable=False)

class Publication(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Make News Image ___X___', editable=False)
    date = models.DateField(_("Date"), default=datetime.date.today, editable=True, blank=False)
    headline = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False, default="Don't forget to add a Description!")

class Event(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Image Dimensions 2000px X 2000px', editable=False)
    date = models.DateField(_("Event Date"), default=datetime.date.today, editable=True, blank=False)
    time = models.CharField(max_length=10, null=False, blank=False, default="9AM")
    title = models.CharField(max_length=300, null=False, blank=False)
    location = models.CharField(max_length=300, null=False, blank=False, default='Founder Rehab Ranch')
    description = models.TextField(max_length=1000, null=False, blank=False, default="Don't forget to add a Description!")

class People(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Image Dimensions: 2000px By 2000px', editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)

class Horse(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Image Dimensions: 2000px By 2000px', editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False, default='This is an amazing horse.')
