from django.urls import path
from .views import LeaveRequest

urlpatterns = [
    path('leave-request/', LeaveRequest, name='leave-request'),
]
