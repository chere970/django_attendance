from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from accounts.models import User
from accounts.serializers import UserSerializer
# from .serializers import ReportSerializer
from leave.models import Leave

from leave.serializers import LeaveRequestSerializer


@api_view(['GET'])
def ReportView(request):
    serializer = UserSerializer(many=True, instance=User.objects.all())
    serializer_data = serializer.data
    # users = User.objects.all()
    return Response(serializer_data)


@api_view(['GET'])
def LeaveRequestView(request):
    serializer = LeaveRequestSerializer(
        many=True, instance=Leave.objects.all())

    leave_requests = serializer.data
    return Response(leave_requests)
