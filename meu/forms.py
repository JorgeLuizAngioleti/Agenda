from django.forms import ModelForm
from . models import  Agenda, Aparelho, Escola, Mensagem
from django.contrib.auth.models import User
#import para email
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem/Dúvidas',widget=forms.Textarea)


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ['eletronico','data','nome','escola','tema','objetivo']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['last_name','username','password']

class TecnologiasForm(ModelForm):
    class Meta:
        model = Aparelho
        fields = ['nome','escola']

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome','dias','permicao']

class MensagemForm(ModelForm):
    class Meta:
        model = Mensagem
        fields = ['data','titulo','escola','texto']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }

'''


AULAS = (
        ('Matutino', (
            ('am', '1ª aula matutino'),
            ('bm', '2ª aula matutino'),
            ('cm', '3ª aula matutino'),
            ('dm', '4ª aula matutino'),
            ('em', '5ª aula matutino'),
            ('fm', '6ª aula matutino'),
            ('x', 'campo anulado'),

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
class NinjaForm(forms.Form):
    #es = request.user.last_name
    tema = forms.CharField(max_length=50)
    objetivo = forms.Textarea()
    #aula = forms.CharField(u'Aula', max_length=3, choices=AULAS)
    eletronico = forms.CharField(max_length=100)
    #tecnologias = forms.ChoiceField(choices=[('0', '--Selecione--')]+ [(c.tecnologia) for c in Agenda.objects.filter(escola =es)])


'''

