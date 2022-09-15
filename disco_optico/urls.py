from django.urls import include, path
from rest_framework import routers
from disco_optico.views import ImageViewSet

router = routers.DefaultRouter()
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]