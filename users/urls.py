from rest_framework import routers
from .api import UserMixins
from django.urls import path
from .routers import CustomRouter

#router=CustomRouter()

router = routers.DefaultRouter()
#router.register('',UserMixins,'users')


#router.register('',UserViewSet,'users')
#urlpatterns=router.urls

urlpatterns =[

    path('',UserMixins.as_view(),name='prueba')
]

urlpatterns+=router.urls