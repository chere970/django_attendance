from django.urls import path
from .views import ReportView
from .views import LeaveRequestView
from .views import SendLeaveRequest
urlpatterns = [
    path('reports/', ReportView, name='reports'),
    path('leave-requests/', LeaveRequestView, name='leave-requests'),
    path('request/add/', SendLeaveRequest, name='send-leave-request'),
    path('leave-request/history', LeaveRequestView, name='leave-request-history')


]
