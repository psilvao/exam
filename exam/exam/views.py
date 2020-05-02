from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from exam.forms import LoginForm
from django.contrib.auth import authenticate,login


def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message="Authentication Sucess"
                else:
                    message="Your user is inactive"
            else:
                message = "Authentication failed"
    else:
        form = LoginForm()
        
    return render(request,'login.html',{'message': message,'form': form})
         


                















