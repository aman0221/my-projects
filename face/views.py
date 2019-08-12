# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import recdata
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from forms import recdata
from .models import student
from .models import attendance_record
from face import recognizer
# Create your views here.
def data(request):
    form = recdata(request.POST, request.FILES)
    if request.method == 'POST':
        myfile = request.FILES.get('image')
        fs = FileSystemStorage(location = '/home/aikansh')
        filename = fs.save('recieved/data.jpg', myfile)
        uploaded_file_url = fs.url(filename)
        roll = request.POST['rno']
        a = student.objects.values('image1').filter(rollno = roll)[0]['image1']
        b = student.objects.values('image2').filter(rollno = roll)[0]['image2']
        c = student.objects.values('image3').filter(rollno = roll)[0]['image3'] 
        k = recognizer(filename , a)
        if k == 1:
           x = attendance_record.objects.get(rollno = roll)
           x.presence = x.presence + 1
           x.save()
           return render(request,'success.html')
        else:
           return render(request,'fail.html')
    else:
       form = recdata() 
       return render(request, 'index.html',{form : 'form'})
     
