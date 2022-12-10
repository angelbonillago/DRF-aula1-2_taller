from .models import Todo
from rest_framework import viewsets,permissions
from .serializers import TodoSerializador,TestTodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class =TodoSerializador


class TestViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer

    