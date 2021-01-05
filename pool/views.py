from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, UserRegistrationForm, RegisterForm, GeeksForms, Student, NameForm
from .models import Tutors
from django.contrib.auth.models import User
from . forms import RegisterForm




def index(request):
    tutor = Tutors.objects.all()
    stu = Student()
    return render(request, 'pool/index.html', {'tutor': tutor}, {'form': stu})

# def anketa(request):
#     if request.method == "POST":
#         Dan = Tutors()
#         Dan.name = request.POST.get("name")
#         Dan.disciple = request.POST.get("disciple")
#         Dan.level = request.POST.get("level")
#         Dan.save()
#     return HttpResponseRedirect('/')

def create(request):
    if request.method == "POST":
        Dan = Tutors()
        Dan.name = request.POST.get("name")
        Dan.disciple = request.POST.get("disciple")
        Dan.level = request.POST.get("level")
        Dan.save()
    return HttpResponseRedirect('/')



def add(request):
    
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    
    return render(request, 'pool/result.html', {"result" : res})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'pool/cabinet.html', {'user': user})
                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'pool/user_login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
    
            return render(request, 'pool/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    
    return render(request, 'pool/register.html', {'user_form': user_form})


def signout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    
    return redirect('index')


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'pool/register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/pool/register_done')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})



def home_view(request): 
	context ={} 

	# create object of form 
	form = GeeksForms(request.POST or None, request.FILES or None) 
	
	# check if form data is valid 
	if form.is_valid(): 
		# save the form data to model 
		form.save() 

	context = {'form': form} 
	return render(request, "index.html", context) 


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})


   
    
# Create your views here.
