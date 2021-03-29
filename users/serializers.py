from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','phone_number', 'username', 'first_name', 'last_name', 'email', 'birth_date')