from rest_framework import serializers
from ..models import MaterialGeneral


class MaterialGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialGeneral
        fields = '__all__'
