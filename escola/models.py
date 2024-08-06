from django.db import models

# Create your models here.
# código omitido

class Estudante(models.Model):
      nome = models.CharField(max_length = 100)
      email = models.EmailField(blank =False, max_length = 30)
      cpf = models.CharField(max_length=11)
      data_nascimento = models.DateField()
      celular = models.CharField(max_length=14)

      # código omitido

      class Curso(models.Model):
        NIVEL = (
              ('B','Básico'),
              ('I','Intermediário'),
              ('A','Avançado'),

      )
      codigo = models.CharField(max_length=10)
      descricao = models.CharField(max_length=100, blank=False)
      nivel = models.CharField(max_length=1, blank=False, null=False)

      def __str__(self):
        return self.nome
# Model Curso