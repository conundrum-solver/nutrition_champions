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
from django.urls import path

import attendance.views
import authentication.views
import dashboard.views
import school_management.views

from nutrition_champions import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', attendance.views.home, name='home'),
    path('dashboard/', dashboard.views.attendance_dashboard, name='attendance_dashboard'),
    path('add-student/', attendance.views.add_student, name='add_student'),
    path('login/', authentication.views.login, name='login'),
    path('school/', school_management.views.school_management, name='school_management'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
