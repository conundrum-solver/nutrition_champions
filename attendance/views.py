from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import render
from .utils import decode_qr_code  # Import the decoding function


def student_management_view(request):
    return render(request, 'student_management.html')


def scan_qr_code(request):
    if request.method == 'POST':
        # qr_code_data = request.POST.get('qr_code_data')
        student_id = request.POST.get('student_id')  # Retrieve student ID from the form

        # Decode the QR code data for the given student ID
        decoded_data = decode_qr_code(student_id)
        print(decoded_data)
        if decoded_data:
            # check if the decoded data matches the QR code data
            if decoded_data == student_id:
                success_message = f"QR code matched for the Student ID {student_id}."
                return render(request, 'scan_qr_code.html', {'decoded_data': decoded_data, 'message': success_message})
            else:
                message = "QR code data does not match with student ID."
                return render(request, 'scan_qr_code.html', {'message': message})

        else:
            message = f"No QR code data found for Student ID {student_id}."
            return render(request, 'scan_qr_code.html', {'message': message})

    elif request.method == 'GET':
        return render(request, 'scan_qr_code.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_management')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})
