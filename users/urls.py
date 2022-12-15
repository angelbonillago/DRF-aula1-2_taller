from rest_framework import routers
from .api import UserViewSet,UserMixins
from django.urls import path
from .routers import CustomRouter

router=CustomRouter()

router = routers.DefaultRouter()
router.register('rutas-personalizadas',UserViewSet,'rutas-personalizadas')


#router.register('',UserViewSet,'users')
#urlpatterns=router.urls

""" urlpatterns =[

    path('',UserMixins.as_view(),name='prueba')
]
 """
urlpatterns = router.urls