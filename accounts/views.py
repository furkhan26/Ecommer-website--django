from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from main.models import *
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('email', False)
        email = request.POST['email']
        name = request.POST['name']
        number = request.POST['number']
        gender = request.POST['gender']
        print(gender)
        password1 = request.POST['pass']
        repassword = request.POST['repass']
        if password1 == repassword:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'this email already registered')
                return redirect('register')
            else:

                user_ = User.objects.create_user(username=email, password=password1)
                
                customer=Customer.objects.create(user=user_,name=name,email=email,number=number,gender=gender,)
                customer.save()
                user_.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')
    else:

        return render(request, "register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')
