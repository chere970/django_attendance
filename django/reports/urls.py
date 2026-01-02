from django.urls import path
from .views import ReportView
from .views import LeaveRequestView
from .views import SendLeaveRequest
urlpatterns = [
    path('reports/', ReportView, name='reports'),
    path('leave-requests/', LeaveRequestView, name='leave-requests'),
    path('leave-request/add/', SendLeaveRequest, name='send-leave-request'),
]
