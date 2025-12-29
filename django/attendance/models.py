from django.db import models

# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    working_hours = models.FloatField(default=0.0)
    status = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'date')
