from categories.serializers import CategorySerializer
from users.serializers import UserSerializer
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    category = CategorySerializer
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'deadline', 'category', 'user')
    
    def create(self, validated_data):
        user = self.context.get('request').user
        task = Task.objects.create(user=user, **validated_data)
        return task