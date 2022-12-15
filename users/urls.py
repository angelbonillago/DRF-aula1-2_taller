from rest_framework import routers
from .api import UserViewSet,UserMixins,CustomAuthToken
from django.urls import path
from .routers import CustomRouter
#
from rest_framework.authtoken import views

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


urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),
    path('api-token-auth-personalizado/', CustomAuthToken.as_view()),
]