"""lastproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import opencv.views
import html_calendar.views
import crudapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('opencv/', include('opencv.urls')),
    path('calendar/', html_calendar.views.calendar_view, name="calendar"),
    path('event/new/', html_calendar.views.event, name="calnew"),
    path('event/edit/<int:event_id>', html_calendar.views.event, name="edit"),
    path('blog/',include('crudapp.urls')),
    path('', crudapp.views.index, name ="index"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

