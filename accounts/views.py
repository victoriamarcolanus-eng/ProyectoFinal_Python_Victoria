from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("inicio")
    
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("inicio")
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserEditForm(instance=usuario)
    
    return render(request, "accounts/editar_perfil.html", {"form": form})