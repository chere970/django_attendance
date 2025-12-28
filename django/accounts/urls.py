from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('checkdashboard/', views.Dashboard, name='dashboard')
]
