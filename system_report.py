import os 
import smtplib
from email.message import EmailMessage
import schedule   #Do not use this as it is not for Production environments because it may terminate automatically when the user logs off and also erase all the schedule code if you are using it in windows task scheduker or linux crontab
from datetime import datetime
import time
import platform

my_email="devsecoperations04@gmail.com"  #Enter your own email id here. Best practice is to use centralized method
my_app_password="bwft cyek ylhe qvwg"  #Generate your app_password via gmail

msg=EmailMessage()
msg['Subject']="Today's system Report"
msg['From']=my_email
msg['To']=my_email
msg['Cc']="computerex103@gmail.com" 
msg.set_content="Today's System report"

def windows_os_detected():
    print("Please check your email")

    with open("C:\\Users\\M.Abubakr\\Desktop\\system_report.txt",mode="rb") as file:
     attach=file.read()
     file_name=file.name
     msg.add_attachment(attach,maintype='application',subtype='octet-stream',filename=file_name)

def linux_os_detected():
    with open("/home/alnafi/linux.txt",mode="rb") as jf:
        attach=jf.read()
        file_name=jf.name
        msg.add_attachment(attach,maintype='application',subtype='octet-stream',filename=file_name)

host_identifier=platform.system()
print(host_identifier)
if host_identifier=="Windows":
    system_info=os.popen("(wmic cpu get loadpercentage && wmic os get TotalVisibleMemorySize,FreePhysicalMemory && wmic logicaldisk get caption,size,freespace)>>C:\\Users\\M.Abubakr\\Desktop\\system_report.txt").read()
    windows_os_detected()
elif host_identifier=="Linux":
    os.popen("(free -m && df -h | cut -c 1-38 | head -n7 | sed -n '1,7p') >>/home/alnafi/linux.txt").read()  #We have used .txt format so that it can run for everyone bt you can change its extension if you want like .csv format
    linux_os_detected()
else:
     print("The system is not identified")

connection=smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login(my_email, my_app_password)
connection.send_message(msg)
connection.quit()

"""
In case you need to use image and audio with your attachment you can uncomment them
#Image Attachment
with open("C:\\Users\\M.Abubakr\\Pictures\\sample_image.jpg",'rb') as image:
    image_data=image.read()
    image_name=image.name
msg.add_attachment(image_data,maintype='image',subtype='jpeg',filename=image_name)

#Audio Attachment
with open("C:\\Users\\M.Abubakr\\Music\\sample_audio.mp3",'rb') as audio:
    audio_data=audio.read()
    audio_name=audio.name
msg.add_attachment(audio_data,maintype='audio',subtype='mp3',filename=audio_name)
"""          

def system_report():
     current_date_time=datetime.now()
     print(f"Your current date and time is{current_date_time}")
     print("Your system report email has been sent")

schedule.every().days.at("00:50").do(system_report)  #Change it according to your time if you want to use this module

while True:
    schedule.run_pending()
    time.sleep(1)

    #If you are using it on windows task scheduler or crontab in linux then you may not need scheduler module

    #Methods to set them on linux and windows are defined in Readme.md
