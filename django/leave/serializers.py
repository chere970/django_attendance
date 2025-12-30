from rest_framework import serializers
from .models import Leave


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['user', 'leave_type', 'start_date',
                  'end_date', 'reason', 'status']
