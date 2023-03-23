from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('lotto_create/', views.lotto_create, name='lotto_create'),
    path('lotto/', views.lotto, name='lotto'),
    path('apps/<int:num>/', views.detail, name='detail'),
    path('apps/<str:name>/', views.greeting, name='greeting'),
]