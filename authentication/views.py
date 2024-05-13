from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import SignUpForm


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to the dashboard
                return redirect('student_management')
            else:
                # Return an error message for invalid credentials
                error_message = 'Invalid email or password. Please try again.'
                return render(request, 'login.html', {'error': error_message})
        else:
            # Return an error message if email or password is missing
            error_message = 'Email and password are required.'
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
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
