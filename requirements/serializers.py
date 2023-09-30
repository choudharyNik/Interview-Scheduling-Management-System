from rest_framework import serializers
from .models import Requirement

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'title', 'description', 'domain', 'vacancies', 'closing_date', 'priority', 'min_experience']
    