"""
URL configuration for modular_survey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from survey import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("f1")),
    path('admin/', admin.site.urls),
    path('Personal_Details',views.p_d,name="f1"),
    path('Favourite_Details',views.f_d,name="f2"),
    path('Address_Details',views.a_d,name="f3"),
    path('Skills_Details',views.s_d,name="f4"),
    path('THANK YOU',views.t_y,name="TY"),
    path('fetch',views.fetch_all,name="fetch")
]
