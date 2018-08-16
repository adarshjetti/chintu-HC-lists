import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from ChintuCourt.config import *
import os

def send_email_with_attachments(get_subject,get_body,get_attaching_file_path):
    email_user = sender_email
    email_password = sender_email_pwd
    email_send = recepient_email

    subject = get_subject

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = get_body
    msg.attach(MIMEText(body,'plain'))

    filepath=get_attaching_file_path
    file_to_be_attached  =open(filepath,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((file_to_be_attached).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+os.path.basename(filepath))
    print("'"+os.path.basename(filepath)+"' is the name of the file attached.")

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

#test method
#t="C:\\Users\\Adars\\PycharmProjects\\SeleniumBasics\\ChintuCourt\\Causelist_folders\\CauseList 2018-08-06"
#send_email_with_attachments("tony","sony",t)

