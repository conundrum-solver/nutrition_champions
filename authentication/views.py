from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to  home
            return redirect('home')
        else:
            # Return an error message or render the login page again with an error
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
