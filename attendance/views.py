from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})


def scan_qr_code(request):
    if request.method == 'POST':
        qr_code_data = request.POST.get('qr_code_data')
        # Logic to decode QR code data and retrieve student information
        # Record attendance for the student
        return HttpResponseRedirect('/success/')
    else:
        return render(request, 'scan_qr_code.html')


def home(request):
    return render(request, 'home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def attendance_dashboard(request):
    students = Student.objects.all()
    return render(request, 'attendance_dashboard.html', {'students': students})
