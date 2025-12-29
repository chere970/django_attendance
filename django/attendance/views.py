from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Attendance
from accounts.models import User
# Create your views here.


@api_view(['POST'])
def check_in(request):
    fingerprint_id = request.data.get('fingerprint_id')

    user = User.objects.get(fingerprint_id=fingerprint_id)
    attendance, created = Attendance.objects.get_or_create(
        user=user,
        date=timezone.now().date()
    )

    if attendance.check_in:
        return Response({"error": "Already checked in"}, status=400)

    attendance.check_in = timezone.now()
    attendance.status = "Present"
    attendance.save()

    return Response({
        "message": f"Check-in successful at {attendance.check_in}"
    })
