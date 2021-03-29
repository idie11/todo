from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from categories.serializers import CategorySerializer
from .models import Category
from .permissions import IsCategoryOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = (IsCategoryOwnerOrReadOnly, IsAuthenticated)