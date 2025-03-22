from django.urls import path
from . import views

urlpatterns = [
    path('', views.criminal_list, name='criminal_list'),
    path('<int:pk>/', views.criminal_detail, name='criminal_detail'),
    path('new/', views.criminal_create, name='criminal_create'),
    path('<int:pk>/edit/', views.criminal_update, name='criminal_update'),
    path('<int:pk>/delete/', views.criminal_delete, name='criminal_delete'),
]
