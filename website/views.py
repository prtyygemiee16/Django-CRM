from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in...")
            return redirect('home')
    return render(request, 'website/home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out...')
    return redirect('home')
    
def register_user(request):
    return render(request, 'register.html', {})

    