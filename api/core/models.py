from django.db import models
from django.core.validators import RegexValidator


class Processo (models.Model):
    PROCESSO_STATUS = [
        ('ATIVO', 'ativo'),
        ('ARQUIVADO', 'arquivado'),
        ('SUSPENSO', 'suspenso'),
    ]
    # para validar o numero do processo
    validador_de_processo = RegexValidator(
        regex=r'^\d{7}-\d{2}.\d{4}.\d{1}.\d{2}.\d{4}$',
        message=('Formato inválido. Use esse padrão: 0000000-00.0000.0.00.0000')
    )

    numero_processo = models.IntegerField(unique=True, max_length=25, validators=[validador_de_processo], help_text='Padrão desejado: 0000000-00.0000.0.00.0000')
    data_criacao = models.DateTimeField()
    vara = models.CharField(max_length=150)
    comarca = models.CharField(max_length=200)
    assunto = models.CharField(max_length=500)
    status = models.CharField(max_length=9, choices=PROCESSO_STATUS)
    
    def __str__(self):
        try:
            return f"{self.data_criacao} - {self.numero_processo} - {self.vara}\ncomarca: {self.comarca}\nassunto: {self.assunto}\nstatus:{self.status}"
        except Exception:
            return str(self.numero_processo)
        

class Audiencia(models.Model):
    AUDIENCIA_TIPO = [
        ('CONCILIAÇÃO', 'conciliação'),
        ('INSTRUÇÃO','instrução'),
        ('JULGAMENTO','julgamento'),
    ]

    data_criacao = models.DateTimeField()
    tipo = models.CharField(max_length=11, choices=AUDIENCIA_TIPO)
    local = models.CharField(max_length=200),
    processos = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name="processo")

    def __str__(self):
        try:
            return f"data: {self.data_criacao}\ntipo: {self.tipo}\nlocal: {self.local}\nprocessos envolvidos: {self.processos}"
        except Exception:
            return str(self.local - self.data_criacao - self.processos)