from .models import Todo
from rest_framework import viewsets,permissions
from .serializers import TodoSerializador,TestTodoSerializer
from rest_framework import status
from .pagination import StandardResultSetPagination
from django.shortcuts import get_object_or_404
#from django_filters.filters import filters
from rest_framework import filters


from rest_framework.response import Response
from rest_framework.views import APIView


class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class =TodoSerializador
    pagination_class=StandardResultSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']


class TodoViewSetCustom(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    #permission_classes=[permissions.AllowAny]
    #serializer_class=TodoSerializador
    pagination_class=StandardResultSetPagination

    def get_serializer_class(self): #retorno el serializador que se usa
        return TodoSerializador

    def list(self, request):
        #queryset = Todo.objects.all()
        #serializer = TodoSerializador(queryset, many = True)
        #print("metodo List!!!")
        #return Response(serializer.data)

        page=self.paginate_queryset(self.queryset)

        if page is not None:
            registro_paginado = self.get_serializer(page,many=True)
            return self.get_paginated_response(registro_paginado.data)
        

        

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializador(todo)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = TodoSerializador(data=request.data,many=True)
        else:
            serializer = TodoSerializador(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def update(self,request,pk=None): #PUT
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializador(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk=None): #PATCH
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializador(todo, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        registro_eliminar = Todo.objects.all()
        eliminar = get_object_or_404(registro_eliminar,pk=pk)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

