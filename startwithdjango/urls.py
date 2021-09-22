
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('contactus/', views.contact,name="contact"),
    path('', views.home),
   
    path('employee/',include('employee.urls')),
    path('contact/',include('contact.urls')),
]
