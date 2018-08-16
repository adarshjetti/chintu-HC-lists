import smtplib

from ChintuCourt.config import *

def send_email(subject,text):
    message = 'Subject: {}\n\n{}'.format(subject,text)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(sender_email,sender_email_pwd)
    server.sendmail(
        sender_email,
        recepient_email_list,
        message)
    server.quit()

#test method
#send_email("tinku","pinku")