from rest_framework.viewsets import ModelViewSet
from tasks.serializers import TaskSerializer
from .models import Task
from .permissions import IsTaskOwnerOrReadOnly



class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    permission_classes = (IsTaskOwnerOrReadOnly, )