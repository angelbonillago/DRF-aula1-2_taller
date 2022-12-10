from rest_framework import routers
from .api import TodoViewSet,TestViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos')  #estamos creando la url de mi api -> 'localhost'api/todos/'

router.register('api/test', TestViewSet, 'test') 


urlpatterns = router.urls #todas las rutas
