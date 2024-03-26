from random import random
from shlex import join
from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .forms import IntegerDateForm

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def hello(request):
    return render(request, 'hello123.html')


def hello1(request):
    return HttpResponse("<center><h1 style='color:blue;'>Welcome to TTM Homepage</h1></center>")


def newhomepage(request):
    return render(request, 'newhomepage.html')


def travelpackage(request):
    return render(request, 'travelpackage.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['sindu']
        print(f'user_input:{user_input}')
        # return HttpResponse('Form Submitted Successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


import random
import string


def random123(request):
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2 = {'ran1': ran1}
    return render(request, 'random123.html', a2)


import random, string


def randomotp1(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, "Randomotp.html", context)

def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
       form = IntegerDateForm(request.POST)
       if form.is_valid():
           integer_value = form.cleaned_data['integer_value']
           date_value = form.cleaned_data['date_value']
           updated_date = date_value +datetime.timedelta(days=integer_value)
           return render(request,'get_date.html',{'updated_date':updated_date})
       else:
           form = IntegerDateForm()
       return render(request, 'get_date.html',{'form':form})


def tzfunctioncall(request):
    return render(request,'pytzexample.html')


from .models import*
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already redistered. Choose a different email."
            return render(request,'myregisterpage.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render (request,'myregisterpage.html')


import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'piechart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'piechart.html', {'form': form})

def Pie(request):
    return render(request,'piechart.html')
def slide(request):
    return render(request,'slide.html')
import requests

def temp(request):
    return render(request,'weather.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '1ab1e6c96ea67ba064bc1ac7dfdd72ef'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None :
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'Login.html')
    else:
        return render(request,'login.html')

def signup1(request):
 if request.method=="POST":
     username=request.POST['username']
     pass1=request.POST['password']
     pass2=request.POST['password1']
     if pass1==pass2:
         if User.objects.filter(username=username).exists():
             messages.info(request,'OOPs! Username already taken')
             return render(request,'signup.html')
         else:
             user = User.objects.create_user(username=username, password=pass1)
             user.save()
             messages.info(request,'Account created successfully')
             return render(request,'login.html')
 else :
     messages.info(request,'password do not match')
     return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

def contactmail1(request):
    return render(request, 'contactmail1.html')

def contactmail(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        to_send=comment +'----------------this is just '
        data = ContactUs(firstname=firstname, lastname=lastname, email=email,comment=to_send)  # Passing adjusted 'to_send' variable

        data.save()
        return HttpResponse("<h1><center>Thank you for giving feedback</center></h1>")













