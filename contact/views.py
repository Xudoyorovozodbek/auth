
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User

class LoadView(View):
    def get(self, request):
        return render(request, "load.html")
class LogoutView(View):
    def get(self, request):
        return render(request, "logout.html")
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
    def post(self,request):
        last_name=request.POST["last_name"]
        first_name=request.POST["first_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        user=User(last_name=last_name,first_name=first_name,username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect("login")
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self,request):
        username=request.POST["username"]
        password=request.POST["password"]
        user=User(username=username,password=password)
        if user:
            return redirect("load")
        else:
            return redirect("register")

