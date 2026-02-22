from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from .forms import LoginForm

@cache_control(no_cache = True,must_revalidate=True,no_store=True)
def login_view(request):
   
    form = LoginForm(request.POST or None)
    if request.method == "POST":
     if form.is_valid():
       username = form.cleaned_data['username']
       password = form.cleaned_data['password']
       user = authenticate(request,username=username,password=password)

       if user is not None:
            login(request,user)
            return redirect('home')
       else:
            form.add_error(None,"Invalid username or password")

    return render(request,'login.html',{'form':form})
@login_required(login_url='/')
@cache_control(no_cache = True,must_revalidate=True,no_store=True)
def home(request):
    return render(request,'home.html')
def logout_view(request):
    logout(request)
    return redirect('/')