from .models import Todo
from rest_framework import viewsets,permissions
from .serializers import TodoSerializador,TestTodoSerializer
from rest_framework import status



from rest_framework.response import Response
from rest_framework.views import APIView


class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class =TodoSerializador


class TestViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer

    

class DeleteAllTodo(APIView):
    def delete(self,request):
        Todo.objects.all().delete() #todo
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializador(todos, many = True)
        return Response(serializer.data)

