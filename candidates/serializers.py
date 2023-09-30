from rest_framework import serializers
from .models import Candidate
from .utils import CandidateRank

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'requirement', 'user', 'first_name', 'last_name', 'address', 'city', 'state', 'pincode', # do i have to add user field here or frontend can handle it?
                  'contact_number', 'email', 'date_of_birth', 'highest_qualification', 'year_of_passing', 
                  'cgpa', 'experience', 'recent_job_responsibilities')
        
    def create(self, validated_data):
        validated_data['rank'] = CandidateRank(validated_data['highest_qualification'], validated_data['cgpa'], validated_data['experience'], validated_data['requirement'].min_experience)
        if validated_data['rank'] == 'Rejected':
            validated_data['application_status'] = 2
        else:
            validated_data['application_status'] = 1
        return Candidate.objects.create(**validated_data)
    























    
    # def validate_first_name(self, value):
    #     if not value.isalpha():
    #         raise serializers.ValidationError("First name should contain only alphabets")
    #     return value
    
    # def validate(self, data):
    #     if data['experience'] < 0:
    #         raise serializers.ValidationError("Experience cannot be negative")
    #     if data['cgpa'] < 0 or data['cgpa'] > 10:
    #         raise serializers.ValidationError("CGPA should be between 0 and 10")
    #     if data['year_of_passing'] < 1900 or data['year_of_passing'] > 2021:
    #         raise serializers.ValidationError("Year of passing should be between 1900 and 2021")
    #     return data