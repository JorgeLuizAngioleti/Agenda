from django.db import models
from datetime import date, datetime

# Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    dias = models.IntegerField(default=1)
    permicao = models.BooleanField(u'Permitir botão de agendar todas as aula',default=False)
    permicao_ninja = models.BooleanField(u'Permição de fixar aulas ', default=False)
    permicao_mensagem = models.BooleanField(u'Permição de visualizar mensagens ', default=False)
    def __str__(self):
        return self.nome


class Aparelho(models.Model):
    nome = models.CharField(max_length=100)
    escola = models.CharField(max_length=50)


    def __str__(self):
        return self.nome


class Agenda(models.Model):

    AULAS = (
        ('Matutino', (
            ('am', '1ª aula matutino'),
            ('bm', '2ª aula matutino'),
            ('cm', '3ª aula matutino'),
            ('dm', '4ª aula matutino'),
            ('em', '5ª aula matutino'),
            ('fm', '6ª aula matutino'),


        )
         ),
        ('Vespertino', (
            ('gv', '1ª aula vespertino'),
            ('hv', '2ª aula vespertino'),
            ('iv', '3ª aula vespertino'),
            ('jv', '4ª aula vespertino'),
            ('lv', '5ª aula vespertino'),
            ('mv', '6ª aula vespertino'),
        )
         ),
        ('Noturno', (
            ('nn', '1ª aula noturno'),
            ('on', '2ª aula noturno'),
            ('pn', '3ª aula noturno'),
            ('qn', '4ª aula noturno'),
            ('rn', '5ª aula noturno'),

        )
         ),

    )
    eletronico = models.CharField(max_length=100)
    data = models.DateField(u'Data' )
    aula = models.CharField(u'Aula', max_length=3, choices=AULAS)
    nome = models.CharField(max_length=50)
    escola = models.CharField(max_length=50)
    tema = models.CharField(max_length=30)
    objetivo = models.TextField()
    def __str__(self):
        return self.nome
    class Meta():
        unique_together = ('eletronico','data','aula','escola',)


class Mensagem(models.Model):
    data = models.DateField(u'Data:')
    titulo = models.CharField(u'Título: ', max_length=40)
    escola = models.CharField(u'Escola: ', max_length=50)
    texto = models.TextField(u'Descrição: ',blank=True)
    def __str__(self):
        return str(self.data) +" "+ self.titulo

    class Meta:
        ordering = ('data',)


