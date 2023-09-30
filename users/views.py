from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

# Create your views here.
class RegisterUserView(CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User created successfully")
        return Response(serializer.errors)