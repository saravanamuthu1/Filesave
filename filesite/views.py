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
            usestatus= User.objects.filter(userName=loginusername,password=loginpassword)
            if usestatus:
                request.session['user_name'] = loginusername
                return redirect('uploadpage',user_name=loginusername)
            else:
                messages.warning(request,'Incorrect username or password')
                return redirect('loginpage')
class Uploadview(ListView):
    def get(self,request,user_name=None):
        return render(request,'main/upload.html')
    def post(self,request,user_name=None):
        title = request.POST['title']
        desc =request.POST['desc']
        file_name= request.FILES['files']
        user_obj = User.objects.get(userName=user_name)
        print(user_obj)
        dataObject=Post(user=user_obj,title=title,desc=desc,file_field=file_name)
        dataObject.save()
        messages.success(request,'you have uploaded your file succcessfully')
        return render(request,'main/upload.html')

class Logoutview(ListView):
    def get(self, request):
        messages.success(request,"you have been logged out")
        try:
            del request.session['user_name']
        except:
            return redirect('homepage') 
        return redirect('homepage')
    