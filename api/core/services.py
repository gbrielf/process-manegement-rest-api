from .models import Processo, Audiencia
from django.core.exceptions import ObjectDoesNotExist


class AudienciaService:
    @staticmethod
    def conferir_duplicidade_vara_e_local(vara, local):
        try:
            #                           acessa a vara do processo relacionado
            return Audiencia.objects.get(processo__vara=vara, local=local)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def agenda_da_comarca(data_criacao, comarca):
        return Audiencia.objects.filter(processo__comarca=comarca, data_criacao=data_criacao)


class ProcessoService:
    @staticmethod
    def status_invalido(processo):
        return processo.status == 'ARQUIVADO' or processo.status == 'SUSPENSO'
    
    @staticmethod
    def processos_por_status_ou_comarca(status, comarca):
        resultado = Processo.objects.all()

        if status:
            return resultado.filter(status=status)
        if comarca:
            return resultado.filter(comarca=comarca)
        if status and comarca:
            return resultado.filter(comarca=comarca,status=status)
        return Processo.objects.none()