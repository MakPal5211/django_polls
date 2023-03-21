from django.urls import path, include
from rest_framework import routers
from .views import MaterialGeneralList, MaterialGeneralDetail

router = routers.DefaultRouter()
router.register(r'material-general', MaterialGeneralList, basename='material-general')
router.register(r'material-general/(?P<pk>\d+)', MaterialGeneralDetail, basename='material-general-detail')

urlpatterns = router.urls
