from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('today_dinner/', views.today_dinner, name='today_dinner'),
]