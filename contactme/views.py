#https://www.sitepoint.com/django-send-email/

from django.shortcuts import render
from .Forms import Input_form
from django.urls import reverse_lazy
from .customfunctions import *


def sms_format(msg, Person_name,email,message,Phone):
    
    message1="\n\n Dear RSTiwari, \n" +str(Person_name) +" has submitted enquiry form. \n "
    body="   Message : " + str(message) + "\n"
    contact_details_phone= "    Phone : " + str(Phone)+ "\n"
    contact_details_email= "    Email : " + str(email)+ "\n"
    full_message=  message1+ body+ contact_details_email + contact_details_phone + "     Thank you"
    
    return (full_message)



def  send_notification (request):
    
      
    if request.method == 'POST':
        form = Input_form(request.POST)
        if form.is_valid():
            
            name= request.POST.get('Name')

            email= request.POST.get('email')

            phone= request.POST.get('phone_number')

            message= request.POST.get('message')
            
            sms_body= sms_format(message,name,email,message,phone)
            
            
            
            
            #send mail
            check_email=send_mail_smpt(email,name,message,str(phone))
            #senf sms
            check_sms=send_sms_twillio(sms_body)
            
            if (check_email or check_sms):
                
                if (check_email and check_sms):
                
                
                    context_sucessfull={"message": ", your input have been succesfully submitted and you will be contacted soon " ,
                                     "url": "https://happyman11.github.io",
                                     "name": name,
                                     "email" : email,
                                    "Text":"Home"}
                
                    return render(request, 'sucessandfailure_template.html',context_sucessfull)
                
                elif(check_email and check_sms==0):
                    
                    context_sucessfull={"message": ", your input have been succesfully submitted via email and you will be contacted soon " ,
                                     "url": "https://happyman11.github.io",
                                     "name": name,
                                     "email" : email,
                                    "Text":"Home"}
                
                    return render(request, 'sucessandfailure_template.html',context_sucessfull)
                
                elif (check_sms and check_email==0):
                    
                    context_sucessfull={"message": ", your input have been succesfully submitted via sms and you will be contacted soon " ,
                                     "url": "https://happyman11.github.io",
                                     "name": name,
                                     "email" : email,
                                    "Text":"Home"}
                
                    return render(request, 'sucessandfailure_template.html',context_sucessfull)
                    
                    
                
            elif(check_email ==0 and check_sms==0):   
                
                context_failure={"message": " Oops!! Submittion Failed." ,
                             "url": "https://www.rstiwari.com/contact",
                             "name": "",
                             "email" : email,
                             "Text" : "Try again"}
                
                return render(request, 'sucessandfailure_template.html',context_failure)
                              
                              
                              

    else:
        form = Input_form()
        return render(request, 'email_form.html', {'form': form})
	

  