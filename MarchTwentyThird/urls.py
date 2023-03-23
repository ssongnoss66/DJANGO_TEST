from django.urls import path
from . import views

app_name = 'MarchTwentyThird'
urlpatterns = [
    path('', views.inpt, name='inpt'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('number_print/<int:number>/', views.number_print, name='number_print'),
    path('calculate/<int:number1>/<int:number2>/', views.calculate, name='calculate'),
]