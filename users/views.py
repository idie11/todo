from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import User
from .permissions import IsUserOwnerOrReadOnly


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )