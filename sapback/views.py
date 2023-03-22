from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import MaterialGeneral
from .rest.serializers import MaterialGeneralSerializer


class MaterialGeneralList(viewsets.ModelViewSet):
    queryset = MaterialGeneral.objects.all()
    serializer_class = MaterialGeneralSerializer

