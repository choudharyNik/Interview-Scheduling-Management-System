from rest_framework import generics, permissions
from .models import InterviewSchedule, InterviewObservation
from .serializers import InterviewScheduleSerializer, InterviewObservationSerializer


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return (request.user.is_superuser or request.user.is_staff 
                    or request.user == InterviewSchedule.objects.get(id=view.kwargs['pk']).candidate.user)
        return (request.user.is_superuser or request.user.is_staff)

# Create your views here.
class InterviewScheduleList(generics.ListCreateAPIView):
    queryset = InterviewSchedule.objects.all()
    serializer_class = InterviewScheduleSerializer
    permission_classes = [CustomPermission, permissions.IsAuthenticated]

class InterviewScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterviewSchedule.objects.all()
    serializer_class = InterviewScheduleSerializer
    permission_classes = [CustomPermission, permissions.IsAuthenticated]

class InterviewObservationList(generics.ListCreateAPIView):
    queryset = InterviewObservation.objects.all()
    serializer_class = InterviewObservationSerializer
    permission_classes = [CustomPermission, permissions.IsAuthenticated]

class InterviewObservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterviewObservation.objects.all()
    serializer_class = InterviewObservationSerializer
    permission_classes = [CustomPermission, permissions.IsAuthenticated]