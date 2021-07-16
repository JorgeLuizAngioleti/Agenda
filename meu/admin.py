from django.contrib import admin
from .models import Agenda, Aparelho, Escola, Mensagem
class AparelhoAdmin(admin.ModelAdmin):
    list_display = ['nome','escola']

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['nome','escola','eletronico','data','aula']

class EscolaAdmin(admin.ModelAdmin):
    list_display = ['nome','dias']
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Aparelho, AparelhoAdmin)
admin.site.register(Escola, EscolaAdmin)
admin.site.register(Mensagem)