from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import mixins

from .models import Todo
from .serializers import TodoSerializer


class TodoViewset(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ReadOnlyModelViewSet,
):
    queryset = Todo.objects.all().order_by("-id")
    serializer_class = TodoSerializer
