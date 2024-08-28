from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from.models import Departments
@never_cache
def user_login(request):
    # check user is auth gonna home page aftr login...here home is view name given in url..
    if request.user.is_authenticated:
        return redirect('home')
    # if http req is post then check the provided crdtn wth database
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # if user is not none wth the data given ...
        # then create session wth login information.....
        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password.')

    return render(request, 'login.html')
@never_cache
# if the unauthntcated user try to login...it goes to login page
@login_required(login_url='login')
def home(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    #if req is post gonna home page
    # redirect means it go to home...
    # user is refresh the page it dont go to the login page
    # return render means it gives template content
    if request.method == 'POST':
        return redirect('home')
    return render(request,'home.html',dict_dept)
# if user click logout button then goto login
def user_logout(request):
    logout(request)
    return redirect('login')


