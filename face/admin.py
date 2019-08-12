# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . models import student, attendance_record
# Register your models here.
admin.site.register(student)
admin.site.register(attendance_record)
