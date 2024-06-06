from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "oktopustiapp/index.html", {'show_navbar': True})

def cards(request):
    return render(request, "oktopustiapp/Dashboard.html", {'show_navbar': False})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(index)
    else:
        form = UserCreationForm()
    return render(request, 'oktopustiapp/registration/register.html', {'form': form, 'show_navbar': False})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'oktopustiapp/registration/login.html', {'form': form, 'show_navbar': False})


def logout_view(request):
    logout(request)
    return redirect(index)

