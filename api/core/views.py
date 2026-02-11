# controller
from rest_framework import viewsets
from .models import Processo, Audiencia
from .serializers import ProcessoSerializer, AudienciaSerializer


class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer


class AudienciaViewSet(viewsets.ModelViewSet):
    queryset = Audiencia.objects.all()
    serializer_class = AudienciaSerializer
