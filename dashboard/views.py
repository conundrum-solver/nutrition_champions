from django_plotly_dash import DjangoDash
from dash import *
from datetime import date, datetime
from django.shortcuts import render
from django.db.models import Count
from attendance.models import ScanRecord
from django.utils import timezone


def dashboard_view(request):
    # Your view logic here
    return render(request, 'attendance_dashboard.html')


app = DjangoDash('dashboard')  # Create a new Dash app

# Define layout of the Dash app
app.layout = html.Div([
    html.H1('Student Scan Data'),
    dcc.Graph(id='scan-graph'),
    dcc.DatePickerRange(
        id='date-picker',
        start_date=date(2022, 1, 1),
        end_date=date.today()
    ),
])


# Define callback to update graph based on selected date range
@app.callback(
    Output('scan-graph', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graph (start_date, end_date):
    # Query student scan data from Django database based on selected date range
    # Here you will write the logic to query the data from your Django model
    # For demonstration purposes, let's assume you have a StudentScan model
    # and you want to query data between the selected date range
    start_date = timezone.make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
    end_date = timezone.make_aware(datetime.strptime(end_date, "%Y-%m-%d"))
    student_scan_data = ScanRecord.objects.filter(timestamp__range=(start_date, end_date))
    scan_counts = student_scan_data.values('timestamp__date').annotate(count=Count('id')).order_by('timestamp__date')

    # Process data and create Plotly figure
    # For demonstration purposes, let's assume you want to create a simple bar chart
    x_values = [entry['timestamp__date'] for entry in scan_counts]
    y_values = [entry['count'] for entry in scan_counts]
    figure = {
        'data': [
            {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Student Scans'}
        ],
        'layout': {
            'title': 'Student Scan Data',
            'xaxis': {'title': 'timestamp'},
            'yaxis': {'title': 'Scan Count'},
            "height": 500,  # px
        }
    }

    # Return updated figure to be displayed in the graph
    return figure
