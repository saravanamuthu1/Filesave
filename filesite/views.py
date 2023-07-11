from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import User, Post
from django.http import HttpResponse
from .models import User
from django.contrib import messages

class Homeview(ListView):
    def get(self,request):
        return render(request,'main/base.html')
    def post(self,request):
        if request.method == 'POST':
            usernamepage=request.POST.get('uname')
            password1=request.POST.get('pwd1')
            password2=request.POST.get('pwd2')
            if password1 == password2:
                dataObject=User(userName=usernamepage,password=password1)
                dataObject.save()
                messages.success(request,'you have successfull created your account')
                return redirect('homepage')
            else:
                messages.warning(request,'password are not same')
                return redirect('homepage')


class Loginview(ListView):
    def get(self,request):
        return render(request,'main/login.html')
    def post(self,request):
        if request.method == 'POST':
            loginusername=request.POST['loginuname']
            loginpassword=request.POST['loginpwd']
            print(loginusername)
            print(loginpassword)
            usestatus= User.objects.filter(userName=loginusername,password=loginpassword)
            if usestatus:
                messages.success(request,'you have successfully logged in')
                return redirect('uploadpage')
            else:
                messages.warning(request,'Incorrect username or password')
                return redirect('loginpage')
        
class Uploadview(ListView):
    def get(self,request):
        return render(request,'main/upload.html')
    
class Logoutview(ListView):
    def get(self,request):
        return render(request,'main/upload.html')
    def post(self,request):
        if request.method == 'POST':
            return redirect('homepage')
