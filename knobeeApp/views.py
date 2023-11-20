from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import mysql.connector as sql
from knobeeApp.models import JobListings
from knobeeApp.models import JobApplications

import smtplib
import ssl
from email.message import EmailMessage
email_sender = 'madhur21063@iiitd.ac.in'
email_password = 'zmqgnpfmfdenqrhf'
email_receiver = 'madhur.gupta18@gmail.com'

def index(request):
    return render(request,"index.html")
def header(request):
    return render(request,"header.html")
def about(request):
    return render(request,"about.html")
def career(request):
    listing = JobListings.objects.all()

    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["contactno"]
        location = request.POST["location"]
        experience = request.POST["exp"]
        education = request.POST["education"]
        empstat = request.POST["empID"]
        job = JobListings.objects.get(Job_ID=empstat)
        application = JobApplications(App_Name=firstname+" "+lastname,App_Email=email,App_Contact=phone,Job_ID=job)
        application.save()
        return render(request,"career.html",{"listing":listing,"success":True})
    return render(request,"career.html",{"listing":listing})
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["msg"]
        phone = request.POST["phone"]
        sub = request.POST["sub"]
        bigMsg = "Name: " + name + "\n" + "Email: "+ email + "\n" + "Phone: "+ phone + "\n" + message
        msg = EmailMessage()
        msg.set_content(bigMsg)
        msg['Subject'] = 'Contact Us'
        msg['From'] = email_sender
        msg['To'] = email_receiver
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_sender, email_password)
            server.send_message(msg)
        return render(request,"contact.html",{"success":True})
    return render(request,"contact.html")
def faq(request):
    return render(request,"faq.html")
