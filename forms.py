from django import forms


class recdata(forms.Form):
     rno = forms.CharField(max_length = 11)
     image = forms.ImageField()
         
