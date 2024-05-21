"""
URL configuration for nutrition_champions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import attendance.views
import authentication.views
import dashboard.views
import school_management.views
from nutrition_champions import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',attendance.views.welcome_login, name='welcome_login'),
    path('home/', authentication.views.user_login, name='home'),
    path('dashboard/', dashboard.views.dashboard_view, name='attendance_dashboard'),
    path('add-student/', attendance.views.add_student, name='add_student'),
    path('scan-student/', attendance.views.scan_qr_code, name='scan_qr_code'),
    path('school/', school_management.views.school_management, name='school_management'),
    path('signup/', authentication.views.SignUpView.as_view(), name='signup'),
    path('decode-qr-code/', attendance.views.decode_qr_code, name='decode_qr_code'),
    path('student_management/', attendance.views.student_management_view, name='student_management'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
