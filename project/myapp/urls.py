from django.urls import path

from project.myapp import views

urlpatterns = [
    path('', views.home,name='home')
]