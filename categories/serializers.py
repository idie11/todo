from rest_framework import serializers
from .models import Category
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id','name', 'description','user')


    def create(self, validated_data):
        user = self.context.get('request').user
        category = Category.objects.create(user=user, **validated_data)
        return category

   