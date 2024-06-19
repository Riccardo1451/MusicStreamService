from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #salvataggio dell'utente creato -> con hashing della pw
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account creato per {username}! Adesso puoi accedere al servizio')
            return redirect('login-view')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, "users/profile.html")