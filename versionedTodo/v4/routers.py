from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'todo', api.TodoViewSet, 'todos')
router.register(r'usuarios', api.UserViewSet, 'usuarios')
api_urlpatterns = router.urls