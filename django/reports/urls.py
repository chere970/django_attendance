from django.urls import path
from .views import ReportView
from .views import LeaveRequestView
urlpatterns = [
    path('reports/', ReportView, name='reports'),
    path('leave-requests/', LeaveRequestView, name='leave-requests'),
]
