from django.http import HttpResponse
from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
# from django.contrib import messages #to send message after creating an account
# from .forms import CreateNewForm
from django.contrib.auth.models import User #to import users from saved data from signup
from django.contrib.auth import login # to authenticate the login user to login
from django.contrib.auth import authenticate,logout



def home(request):
    data={
        'title':'IWS Home Page'
    }
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate (request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/userhome/')

        elif user is None:
            pass
        else:
            return HttpResponse('Check Your User id and password')

    return render(request,'home.html',data)

def userhome(request):
    data={
        'title':'IWS Home'
    }
    return render(request,'userhome.html',data)

# def contact(request):
        
#     return render(request,'contact.html')

def essaytopic(request):
    return render(request,'essaytopic.html')

# def vocabulary(request):
#     return render(request,'vocabulary.html')

def topics(request):
    return render(request,'topics.html')

def signup (request):

    if request.method =='POST':# to get information or data from signup page
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dateofbirth = request.POST.get('dateofbirth')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2: # to match password with confirm password
            return HttpResponse ('Password do not match Confirm Password')

        else:
            my_user = User.objects.create_user(username, email, password)#to create users
            my_user.save()#to save created users
            # return  ('You login has been created Successfully!!')#to display message after succeful signup
            return redirect('/signin')
        
        # print(firstname,lastname,username,password)
    return render(request,'signup.html',{})

def signin(request):
    if request.method =='POST':# to get information or data from signup page 
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/userhome/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'signin.html',{})

def vocabulary(request):
    return render(request,'vocabulary.html')

def contact(request):        
    return render(request,'contact.html')

def workinglife (request):
    return render(request,'workinglife.html')


