from twilio.rest import Client
import os
import environ

from django.conf import settings
import smtplib
import  random as r
import re
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_sms_twillio(message):
    
    
            
    
      env = environ.Env(
                        DEBUG=(bool, False)
                       )

      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


      environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    

      account_sid= env('Account_SSID')
      auth_token= env('Auth_token')
      Phn_no_twillio=env('Phn_no_twillio')
      
      mynumber2=env('my_number2')
      my_number1=env('my_number1')

    
      
      client_object = Client(account_sid, auth_token)
      
      
      try:
          
          sms_number_1= client_object.messages.create(
                                           body=message,
                                           from_=Phn_no_twillio,
                                           to=my_number1 
                                           )

          print(sms_number_1.sid)

                                        
       #    sms_number2= client_object.messages.create(
       #                                     body=message,
       #                                     from_=Phn_no_twillio,
       #                                     to=my_number1 
       #                                     )

       #    print(sms_number2.sid)
          return(1)   
         
 
          
      except:
                
          msg1="SMS-Dishpatcher-class >> Function - send_sms_twillio: message sending failed" + " number :" +str(my_number1)
          print(msg1)
          msg="SMS-Dishpatcher-class >> Function - send_sms_twillio: message sending failed" + " number :" +str(my_number1)
          print(msg)
          return(0)
      
      
          
def send_mail_smpt(email,name,message,phone_number):
     
      # put your real email here
      env = environ.Env(
                        DEBUG=(bool, False)
                       )

      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


      environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
      
      Host_email=env('EMAIL_HOST_USER')
      Host_email_passowrd=env('EMAIL_HOST_PASSWORD')
      Mail_server_smtp=env('EMAIL_server')
      Email_admin1=env('EMAIL_CC1')
      Email_admin2=env('EMAIL_CC2')
      msg = MIMEMultipart()
      msg['From'] = Host_email
      msg['Subject'] = " Reciept Inquiry Sumbition - RSTiwari"
      msg['To'] = email
     
      msg['reply-to']=Email_admin1

      
      
      message_body_user="""\
<html>
  <body>
    <p>Hi """+name+""",</p>
        
       <h3 > Thank you for contacting me. I will get back to you shortly. </h3> 
      
<blockquote>
<pre style="padding-bottom:25;"> 
<centre>
       Name : """+name+"""
       Email : """+email+"""
       contact Number : """+ phone_number+"""
</centre>
Message :  """+message+"""
</pre>   
</blockquote>

      
       
       
       <h4> Please feel free to give feedback on below applications. </h4>
       
       <p style="padding-bottom:25;">
       
    
       <dt>1. <b>Link of Deployed Applications </b></dt>
       
       <p style="padding-top:15;">
       <dd>1.1 <a href="https://share.streamlit.io/happyman11/mnist-svm-streamlit">SVM-Mnist Classification</a></dd>
       <dd>1.2. <a href="https://share.streamlit.io/happyman11/logistic_regression_streamlit_sklearn_dataset">Logistic Regression on sklearn Dataset</a> </dd>
       <dd>1.3. <a href="https://rstiwarisampledeploy.herokuapp.com">Iris Decision Tree Classification</a> </dd>
       <dd>1.4. <a href="https://penguing-prediction-streamlit.herokuapp.com/">Penguine Island Classification</a> </dd>
       <dd>1.5. <a href="https://webscrappingsample.herokuapp.com/">Web Scrapping Sample</a> </dd>
       <dd>1.6. <a href="https://happyman11.github.io/foodorder.github.io/">Food ordering Website</a> </dd>
       <dd>1.7. <a href="https://prisondashboard.herokuapp.com/">Prison Data Analysis Dashboard using Dash and Plotly</a> </dd>
       <dd>1.8. <a href="https://mycentralisedapplication.herokuapp.com/">Centralized mailing Platform</a> </dd>
       <dd>1.9. <a href="https://share.streamlit.io/happyman11/natural-language-processing-sentiment-analysis/main/app.py">NLP- Sentiment Analyser</a> </dd>
        <dd>1.10. <a href="https://share.streamlit.io/happyman11/natural-language-application-streamlit-deploy-summarizing/main/app.py">NLP- Text Summeriser</a> </dd>
       
       </p>
       </p>
       
       
       <p style="padding-bottom:25;">
       
       <dt>2. <b>Medium Blog  </b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://tiwari11-rst.medium.com/">Medium</a> </dd>
       </p>
       </p>
      
       <p style="padding-bottom:25;">
       <dt>3. <b>Youtube </b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://www.youtube.com/channel/UCFG5x-VHtutn3zQzWBkXyFQ">Youtube Channel</a> </dd>
       </p>
       </p>
   
       <p style="padding-bottom:25;">
       <dt>4. <b>Find Me</b></dt>
       <p style="padding-top:15;">
       <dd>1. <a href="https://www.rstiwari.com">Profile</a> </dd>
       <dd>2. <a href="https://tiwari11-rst.medium.com">Medium</a> </dd>
       <dd>3. <a href="https://happyman11.github.io/">Github Pages</a> </dd>
       <dd>4. <a href="https://forms.gle/mhDYQKQJKtAKP78V7"> Find me</a> </dd>
       
       </p>
       </p>
   
       <p tyle="padding-bottom:25;padding-bottom:15;">
       <a href="https://tiwari11-rst.medium.com/subscribe">
       <h2 style="color:black;"> Subscribe Medium Blog !!!!!</h2>
       <blockquote> 
       <h3 style="color:green;"> Click Here for Subscribing </h3>
       </blockquote> 
       </a>
       
       </p>
       
     
       <p> For Unsubscribe, please send mail to DeployedApplications@gmail.com  with subject  Unsubscribe from medium </p>
       <br>
      
       <b>Regards</b>,<br>
       Ravi Shekhar Tiwari<br>
       Website: https://www.rstiwari.com<br>
       Email: tiwari11.rst@gmail.com <br>
    
  </body>
</html>
"""
      message_body_admin="""\
<html>
  <body>
    <p>Hi RS Tiwari,</p>
        
       <h3 > Below User has tried to connect with you.Please connect with him . </h3> 
      
<blockquote>
<pre style="padding-bottom:25;"> 
<centre>
       Name : """+name+"""
       Email : """+email+"""
       contact Number : """+ phone_number+"""
</centre>
Message :  """+message+"""
</pre>   
</blockquote>

       <b>Regards</b>,<br>
       Ravi Shekhar Tiwari<br>
       Website: https://www.rstiwari.com<br>
       Email: tiwari11.rst@gmail.com <br>
    
  </body>
</html>
"""
      
      try: 
          
         s = smtplib.SMTP(Mail_server_smtp, 587)  
         s.starttls() 
         s.login(msg['From'], Host_email_passowrd) 
         msg.attach(MIMEText(message_body_user, 'html'))
         s.sendmail(msg['From'], msg['To'], msg.as_string()) 
         s.quit() 
         
         msg1="Email-Dishpatcher-class >> Function - send_sms_twillio: message sending sucess" + " number :" +str(email)
         print(msg1)
         
         
         
        
         
         
         
         
         return(1)
         
      except: 
          
          msg1="SEmail-Dishpatcher-class >> Function - send_sms_twillio: message sending failed" + " number :" +str(email)
          print(msg1)
          return(0)
      
      finally:
          
          msg1 = MIMEMultipart()
          msg1['From'] = Host_email
          msg1['Subject'] = " Copy of Inquiry Sumbition - RSTiwari"
          msg1['To'] = Email_admin1
          msg1['reply-to']=Email_admin1
          
          s1 = smtplib.SMTP(Mail_server_smtp, 587)  
          s1.starttls() 
          s1.login(msg['From'], Host_email_passowrd) 
          msg1.attach(MIMEText(message_body_admin, 'html'))
          s1.sendmail(msg1['From'], msg1['To'], msg1.as_string()) 
          s1.quit() 
          
          
         
       
      
      
      
      
     
      


      
          


          
          
          
          
          
          
          