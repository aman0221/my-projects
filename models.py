# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student(models.Model):
       rollno = models.CharField(max_length = 11)
       name = models.CharField(max_length = 80)
       image1 = models.CharField(max_length = 80) 
       image2 = models.CharField(max_length = 80)
       image3 = models.CharField(max_length = 80)

       def __str__(self):
           return u'%s   %s' %(self.name, self.rollno)

class attendance_record(models.Model):
       rollno = models.CharField(max_length = 11)
       presence = models.IntegerField()

       def __str__(self):
           return self.rollno

