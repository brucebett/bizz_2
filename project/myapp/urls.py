from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('contact/', views.contact,name='contact'),
    path('team/', views.team,name='team'),
]