from rest_framework import routers
from .api import TodoViewSet,DeleteAllTodo,TodoViewSetCustom,TestViewSet,TodoMixinsViewSet
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register('api/todos/filtros', TodoViewSet, 'todos')  #estamos creando la url de mi api -> 'localhost'api/todos/'

#router.register('api/test', TestViewSet, 'test') 

router.register('api/todos/todoviewset', TodoViewSetCustom, 'todoviewset') 

router.register('api/mixin',TodoMixinsViewSet,'mixin')

urlpatterns = router.urls #todas las rutas

""" urlpatterns+=[  
    path('api/todos/deleteAll',DeleteAllTodo.as_view(),name="deleteAll"),
    path('api/todos/geteAll',DeleteAllTodo.as_view(),name="geteAll"),


    #modelviewset
    #path('api/todos/todocustom',TodoViewSetCustom,'todocustom')


    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] """




