from django.urls import path, include
from rest_framework import routers

from . import api_views as api_views


__all__ = ["router", "urlpatterns"]

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'persons', api_views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
