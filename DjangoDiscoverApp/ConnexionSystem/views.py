from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def signIn(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Login Successfull')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, f'invalid credentials')
            return HttpResponseRedirect(reverse('signin'))
    else:
        return render(request, 'signin/signin.html')


def signOut(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, f'logged out from websites..')
        return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username exists! try another usernmae...')
                return HttpResponseRedirect(reverse('register'))
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Email is already taken ! try another one')
                    return HttpResponseRedirect(reverse('register'))
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    messages.success(request, f'Account added successfully !..')
                    return HttpResponseRedirect(reverse('signin'))
        else:
            messages.error(request, f'Password did not matched !..')
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request, 'register/register.html')