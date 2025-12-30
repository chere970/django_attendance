from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import LeaveRequestSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def LeaveRequest(request):
    serializer = LeaveRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    leave_request = serializer.save()
    return Response(LeaveRequestSerializer(leave_request).data)
