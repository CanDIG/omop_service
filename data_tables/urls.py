from django.urls import path, include
from rest_framework import routers

from . import api_views as api_views


__all__ = ["router", "urlpatterns"]

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'persons', api_views.PersonViewSet)
router.register(r'conditionoccurrences', api_views.ConditionOccurrenceViewSet)
router.register(r'procedureoccurrences', api_views.ProcedureOccurrenceViewSet)
router.register(r'measurements', api_views.MeasurementViewSet)
router.register(r'observations', api_views.ObservationViewSet)
router.register(r'specimens', api_views.SpecimenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ingest', api_views.ingest, name="ingest"),
    path('overview', api_views.overview,
         name="overview"),
]
