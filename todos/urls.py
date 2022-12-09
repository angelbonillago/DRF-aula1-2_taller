from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos')  #estamos creando la url de mi api -> 'localhost'api/todos/'

urlpatterns = router.urls #todas las rutas
