from django.db import models
from candidates.models import Candidate


# Create your models here.
class InterviewSchedule(models.Model):
    class InterviewStatus(models.IntegerChoices):
        SCHEDULED = 1
        COMPLETED = 2
        CANCELLED = 3

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interview_date = models.DateField()
    mode = models.CharField(max_length=20, default='Pending')
    venue = models.TextField(blank=True, null=True)
    status = models.IntegerField()

class InterviewObservation(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    marks = models.IntegerField() #in percentage
    notice_period = models.IntegerField()
    result = models.CharField(max_length=20, default='Pending')