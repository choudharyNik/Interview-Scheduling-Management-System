from django.db import models

# Create your models here.
class Requirement(models.Model):
    class Domain(models.IntegerChoices):
        DOTNET = 1
        JAVA = 2
        PYTHON = 3
        DJANGO = 4
        FLASK = 5
        REACT = 6

    class Priority(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    title = models.CharField(max_length=100, default='Title')
    description = models.TextField(default='Description')
    domain = models.IntegerField(choices=Domain.choices)
    vacancies = models.PositiveIntegerField()
    closing_date = models.DateField()
    priority = models.IntegerField(choices=Priority.choices)
    min_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + "__" + str(self.title)