from django.urls import path
from . import views

urlpatterns = [
    path('', views.companys_list, name='companys_list'),
    path('create/', views.companys_create, name='companys_create'),
    path('update/<int:pk>/', views.companys_update, name='companys_update'),
]