"""
URL configuration for MyIndustry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myindustryapp import views
admin.site.site_header = "MyIndustry Admin"
admin.site.site_title = "MyIndustry Admin Portal"
admin.site.index_title = "Welcome to MyIndustry Portal"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name='index'),
    path("profile",views.index,name='profile'),
    path("updates",views.updates,name='updates'),
    path("contact",views.contact,name='contact')
]
