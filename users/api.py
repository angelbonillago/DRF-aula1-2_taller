from .serializers import UserSerializer
from .models import Users
from rest_framework import viewsets,mixins,generics
from rest_framework.response import Response


#Mixins para usuarios.
class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    serializer_class=UserSerializer
    queryset=Users.objects.all()
    lookup_field='id'

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    


#Mixin personalizado para usuarios
class ListarUsuarios:

    def listar_usuario(self, request, *args, **kwargs):
        #filtro
        filtro={}

        if("buscar" in self.request.query_params): #en la ruta, la palabra 'buscar'
            #busqueda personlizada
            valor=self.request.query_params['buscar']
            campo=self.busquedad_id if valor.isnumeric() else f'{self.busquedad_username}__contains'
            filtro[campo]=valor

        queryset = self.get_queryset().filter(**filtro)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserMixins(ListarUsuarios,generics.GenericAPIView):
    serializer_class=UserSerializer
    queryset=Users.objects.all()
    busquedad_id='id'
    busquedad_username='username'
    
    def get(self, request, *args, **kwargs):
        return self.listar_usuario(request, *args, **kwargs)


   




