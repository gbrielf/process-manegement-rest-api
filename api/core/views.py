# controller
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import AudienciaService, ProcessoService
from .models import Processo, Audiencia
from .serializers import ProcessoSerializer, AudienciaSerializer


class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer

    @action(detail=False, methods=['GET'])
    def listar_por_status_ou_comarca(self, request):
        # o	Deve permitir listar e filtrar por status e comarca
        status_processo = request.query_params.get('status')
        comarca = request.query_params.get('comarca')

        if not status_processo and not comarca:
            return Response({"error": "Informe 'status' ou 'comarca'"})

        resultado = ProcessoService.processos_por_status_ou_comarca(status_processo, comarca)

        if not resultado:
            return Response({"error": "Nenhum processo com os dados especificados"})
        
        serializer = ProcessoSerializer(resultado, many=True)
        return Response(serializer.data, status=200)


class AudienciaViewSet(viewsets.ModelViewSet, APIView):
    queryset = Audiencia.objects.all()
    serializer_class = AudienciaSerializer

    def post(self, request):
        processo_id = request.data.get('processo')
        local = request.data.get('local')

        try:
            processo = Processo.objects.get(id=processo_id)
        except Processo.DoesNotExist:
            return Response({"error": "Processo inexistente"}, status=400)
        
        if ProcessoService.status_invalido(processo):
            return Response({"error": "Processo arquivado ou suspenso..."}, status=400)
        vara = processo.vara

        if AudienciaService.conferir_duplicidade_vara_e_local(vara, local):
            return Response({"error": "Já existe uma audiência nessa vara e local"}, status=400)

        serializer = AudienciaSerializer(data=request.data)

        if serializer.is_valid():                    
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
        
    @action(detail=False, methods=['GET'])
    def agenda_de_audiencias(self, request):
        # o	Endpoint que retorna a agenda de audiências de uma comarca em um determinado dia
        data_criacao = request.query_params.get('data_criacao')
        comarca = request.query_params.get('comarca')
        audiencias = AudienciaService.agenda_da_comarca(data_criacao, comarca)
        if not audiencias:
            return Response({"error": "Nenhuma audiencia foi cadastrada nesse dia"}, status=400)
        
        serializer = AudienciaSerializer(audiencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
        
