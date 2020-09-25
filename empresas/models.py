from django.db import models


class Empresas(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cnpj = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField(
        max_length=55
    )

    complemento = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    estado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    pais = models.CharField(
        max_length=255,

        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

