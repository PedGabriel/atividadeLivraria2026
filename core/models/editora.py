from django.db import models


class Editora(models.Model):
    site = models.URLField(blank=True, null=True, max_length=100)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} - {self.site}"
