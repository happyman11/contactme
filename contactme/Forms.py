# -*- coding: utf-8 -*-

from django import forms

   


    
class Input_form(forms.Form):
       
    Name = forms.CharField(max_length = 20,required=True,label='Name')
    phone_number=forms.CharField(max_length = 12,required=True,label='Phone Number')
    email = forms.EmailField(required=True,label='Email')
    message = forms.CharField(widget=forms.Textarea,label='Message')
    

    