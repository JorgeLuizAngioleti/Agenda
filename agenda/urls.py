"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as author_views
from meu.views import home, agenda_form, pesquisa, tec_pesquisa,\
    sair_logout, agenda_delete,atualizar, add_user, contato,add_tec,\
    admin_sistema, del_tecnologia, del_pessoa, dias, atualizar_dias,\
    mensagem, del_mensagem,add_ninja


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_sistema/', admin_sistema, name='admin_sistema'),
    path('delete_tec/<int:id>/', del_tecnologia, name='del_tec'),
    path('delete_mensagem/<int:id>/', del_mensagem, name='del_mensagem'),
    path('delete_pessoa/<int:id>/', del_pessoa, name='del_pessoa'),
    path('login/', author_views.login, name='login'),
    path('logout/',  sair_logout, name='logout'),
    path('', home, name='home'),
    path('dias/', dias, name='dias'),
    path('add_tec/', add_tec, name='add_tec'),
    path('adicionar/', add_user, name='add_user'),
    path('delete/<int:id>/<str:data>/<str:tecnologia>/', agenda_delete, name='agenda_delete'),
    path('atualizar/<int:id>/<str:data>/<str:tecnologia>/', atualizar, name='atualizar_dados'),
    path('atualizar_dias/<int:id>/', atualizar_dias, name='atualizar_dias'),
    path('agenda/<str:data>/<str:tecnologia>/', agenda_form, name='agenda_form'),
    path('pesquisa/', pesquisa,name='pesquisa'),
    path('contato/', contato,name='contato'),
    path('tec/', tec_pesquisa,name='tec_pesquisa'),
    path('mensagem/', mensagem,name='mensagem'),
    path('ninja/', add_ninja,name='add_ninja'),

]

admin.site.site_header = 'Jorge  AgendaApp'