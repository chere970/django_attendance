from django.db import models

# Create your models here.


class Leave(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
