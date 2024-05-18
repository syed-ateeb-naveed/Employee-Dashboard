from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('create2/', views.create2, name='create2')
]