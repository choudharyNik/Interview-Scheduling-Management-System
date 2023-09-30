from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import CandidateSerializer
from .models import Candidate
from rest_framework.permissions import IsAuthenticated, BasePermission  


class GetPutDelPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return (request.user.is_staff or request.user.is_superuser or request.user.is_admin)
        return (request.user.is_staff or request.user.is_superuser or request.user.is_admin
                #  or request.user.email == Candidate.objects.get(id = view.kwargs.get('pk')).email #this & the following statement, both are correct
                 or request.user == Candidate.objects.get(id = view.kwargs.get('pk')).user
        )

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff == False and request.user.is_superuser == False and request.user.is_admin == False)


# Create your views here.
class CandidateCreateAPIView(CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated, PostPermission]

class CandidateDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated, GetPutDelPermission]



