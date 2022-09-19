from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

class Banner(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Make Banner Image 2000px X 700px', editable=False)

class Publication(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Make News Image ___X___', editable=False)
    headline = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False, default="Don't forget to add a Description!")

class People(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Make Image ___X___', editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)

class Horse(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    note = models.CharField(max_length=100, default='Make Horse Image ___X___', editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False, default='This is an amazing horse.')
