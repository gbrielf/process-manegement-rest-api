# DTO/Controller
from rest_framework import serializers
from .models import Processo, Audiencia


class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'


class AudienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiencia
        fields = '__all__'