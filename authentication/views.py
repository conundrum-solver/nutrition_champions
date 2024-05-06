from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import SignUpForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        email = request.POST('email')
        password = request.POST('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to  home
            return redirect('home')
        else:
            # Return an error message or render the login page again with an error
            return render(request, 'login.html', {'error': 'Invalid Email or password'})
    else:
        return render(request, 'login.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
