# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cemetery(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="Cemetery Name",max_length=100)
    city=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=5)
    date_created=models.DateTimeField(editable=False, auto_now_add=True)
    date_modified= models.DateTimeField(editable=False, auto_now=True)
    created_by=models.ForeignKey('auth.User')

    def __str__(self):
        return  str(self.id) +'-' + self.name + ' -  ' + self.city
