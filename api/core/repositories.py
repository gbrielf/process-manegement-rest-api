from core.models import Processo, Audiencia

class ProcessoRepository:
    @staticmethod
    def get_all():
        return Processo.objects.all()
    
    @staticmethod
    def get_by_id(processo_id):
        return Processo.objects.get(id=processo_id)
    
    @staticmethod
    def create(data):
        return Processo.objects.create(**data)

    @staticmethod
    def delete(processo_id):
        processo = Processo.objects.get(id=processo_id)
        processo.delete()

class AudienciaRepository:
    @staticmethod
    def get_all():
        return Audiencia.objects.all()
    
    @staticmethod
    def get_by_id(audiencia_id):
        return Audiencia.objects.get(id=audiencia_id)
    
    @staticmethod
    def create(data):
        return Audiencia.objects.create(**data)

    @staticmethod
    def delete(audiencia_id):
        audiencia = Audiencia.objects.get(id=audiencia_id)
        audiencia.delete()