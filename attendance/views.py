from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def create_student(request):
    if request.method == 'POST':
        # Create a new student object using form data
        student = Student.objects.create(
            name=request.POST['name'],
            student_id=request.POST['student_id'],
            date_of_birth=request.POST['date_of_birth'],
            qr_code=request.POST['qr_code'],
        )
        # Redirect to a success page or another page
        return HttpResponseRedirect('/success/')
    else:
        # Render form to create a new student
        return render(request, 'create_student.html')


def scan_qr_code(request):
    if request.method == 'POST':
        qr_code_data = request.POST['qr_code_data']
        # Logic to decode QR code data and retrieve student information
        # Record attendance for the student
        return HttpResponseRedirect('/success/')
    else:
        # Render QR code scanning page
        return render(request, 'scan_qr_code.html')


def home(request):
    return render(request, 'home.html')


def add_student(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or another page
            return redirect('home')  # Redirect to the home page after adding the student
    else:
        # If the request method is not POST, display an empty form
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def attendance_dashboard(request):
    # Query the database to fetch attendance metrics
    students = Student.objects.all()
    # Render dashboard template with attendance data
    return render(request, 'attendance_dashboard.html', {'students': students})
