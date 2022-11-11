from rest_framework import routers
from .views import PostViewSet
from django.urls import path,include

router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns =[
    path('', include(router.urls)),
]