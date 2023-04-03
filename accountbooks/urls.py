from django.urls import path
from . import views

app_name = 'accountbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:accountbook_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:accountbook_pk>/edit/', views.edit, name='edit'),
    path('<int:accountbook_pk>/update/', views.update, name='update'),
    path('<int:accountbook_pk>/delete/', views.delete, name='delete'),
    path('<int:accountbook_pk>/copy/', views.copy, name='copy')
]