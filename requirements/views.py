from rest_framework.response import Response
from .serializers import RequirementSerializer
from rest_framework import generics
from .models import Requirement
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication

class HasAccess(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True # to allow a non-staff user to perform GET requests
        return request.user.is_staff


# Create your views here.
class RequirementListView(generics.ListCreateAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [IsAuthenticated, HasAccess]
    

class RequirementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [IsAuthenticated, HasAccess]
