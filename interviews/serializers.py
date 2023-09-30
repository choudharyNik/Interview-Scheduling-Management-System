from rest_framework import serializers
from .models import InterviewSchedule, InterviewObservation
from .utils import InterviewMode, InterviewResult

class InterviewScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSchedule
        fields = ('id', 'candidate', 'interview_date', 'venue', 'status', 'mode')

    def create(self, validated_data):
        validated_data['mode'] = InterviewMode(validated_data['candidate'])
        return InterviewSchedule.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.candidate = validated_data.get('candidate', instance.candidate)
        instance.interview_date = validated_data.get('interview_date', instance.interview_date)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.status = validated_data.get('status', instance.status)
        instance.mode = InterviewMode(instance.candidate)
        instance.save()
        return instance


class InterviewObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewObservation
        fields = ('id', 'candidate', 'marks', 'notice_period', 'result')

    def create(self, validated_data):
        validated_data['result'] = InterviewResult(validated_data['marks'], validated_data['candidate'])
        return InterviewObservation.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.candidate = validated_data.get('candidate', instance.candidate)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.notice_period = validated_data.get('notice_period', instance.notice_period)
        instance.result = InterviewResult(instance.marks, instance.candidate)
        instance.save()
        return instance