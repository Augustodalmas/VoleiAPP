from django.db import models
from User.models import perfilUsuario
from django.core.files.base import ContentFile
from django.utils import timezone
import qrcode
from io import BytesIO


class Partida(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    INICIANTE = 'Iniciante'
    INTERMEDIARIO = 'Intermediario'
    AVANCADO = 'Avancado'
    NIVEL = [
        (INICIANTE, 'Iniciante'),
        (INTERMEDIARIO, 'Intermediario'),
        (AVANCADO, 'Avancado'),
    ]
    nivel = models.CharField(max_length=15, choices=NIVEL, default=INICIANTE)

    CINCOX1 = '5x1'
    SEISX0 = '6x0'
    QUATROX2 = '4x2'
    ROTACAO = [
        (CINCOX1, '5x1'),
        (SEISX0, '6x0'),
        (QUATROX2, '4x2'),
    ]
    rotacao = models.CharField(max_length=3, choices=ROTACAO, default=SEISX0)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=100)  # Trocar para Fk
    organizador = models.ForeignKey(perfilUsuario, on_delete=models.CASCADE)
    lotacao = models.IntegerField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    # Adicionado itens de Pagamento
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    id_stripe = models.CharField(max_length=256, blank=True, null=True)
    preco_stripe = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['data', 'hora', 'local'], name='unique_partida')
        ]

    def gerar_qr_code(self):
        qr_data = f"http://192.168.1.4:8000/partidas/{self.id}/checkin"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer)
        self.qr_code.save(f'partida_{self.id}.png', ContentFile(
            buffer.getvalue()), save=False)
        buffer.close()
        self.save()

    def __str__(self):
        return self.titulo


class Participacao(models.Model):
    usuario = models.ForeignKey(perfilUsuario, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    check_in = models.BooleanField(default=False)
    check_in_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'partida'], name='unique_participacao')
        ]

    def realizar_check_in(self):
        self.check_in = True
        self.check_in_time = timezone.now()
        self.save()


class HistoricoPartida(models.Model):
    partida = models.ForeignKey(
        Partida,
        on_delete=models.CASCADE,
        related_name='historicos'
    )
    data = models.DateField()
    participacao = models.BooleanField(default=False)
