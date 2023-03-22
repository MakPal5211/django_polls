from django.urls import path, include
from rest_framework import routers
from .views import MaterialGeneralList

router_viewsets = routers.DefaultRouter()
router_viewsets.register(r'material-general', MaterialGeneralList, basename='material-general')

urlpatterns = router_viewsets.urls
