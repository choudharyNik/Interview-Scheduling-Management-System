from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user