from django.db import models
from requirements.models import Requirement
from users.models import User


# Create your models here.
class Candidate(models.Model):
    class HighestQualification(models.IntegerChoices):
        BTECH = 1
        MTECH = 2
        BSC = 3
        MSC = 4
        BCA = 5
        MCA = 6
    
    class ApplicationStatus(models.IntegerChoices):
        ACCEPTED = 1
        REJECTED = 2

    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    date_of_birth = models.DateField()
    highest_qualification = models.IntegerField(choices=HighestQualification.choices)
    year_of_passing = models.IntegerField()
    cgpa = models.FloatField()
    experience = models.IntegerField()
    recent_job_responsibilities = models.TextField()
    application_status = models.IntegerField(choices=ApplicationStatus.choices, blank=True, null=True)
    rank = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(str(self.id) + "__" + str(self.first_name) + " " + str(self.last_name))