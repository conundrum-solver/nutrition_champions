from django.shortcuts import render


# Create your views here.
def attendance_dashboard(request):
    return render(request, 'attendance_dashboard.html')
