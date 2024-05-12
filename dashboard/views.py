from django.shortcuts import render
from attendance.models import ScanRecord


def dashboard_view(request):
    # Retrieve all scan records
    all_scan_records = ScanRecord.objects.all()

    # Pass the scan records to the template context
    context = {
        'scan_records': all_scan_records
    }

    return render(request, 'attendance_dashboard.html', context)
