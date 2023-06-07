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
            print(usernamepage)
            print(password1)
            print(password2)
            if password1 == password2:
                dataObject=User(userName=usernamepage,password=password1)
                dataObject.save()
                messages.success(request,'you have successfull created your account')
                return redirect('homepage')
            else:
                messages.warning(request,'password are not same')
                return redirect('homepage')


class Signupview(ListView):
    def get(self,request):
        return render(request,'main/signup.html')