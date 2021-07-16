from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import  Aparelho, Agenda, Escola, Mensagem
from django.contrib.auth.decorators import  login_required
from .forms import AgendaForm, UserForm, TecnologiasForm, ContatoForm, EscolaForm, ModelForm, MensagemForm
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, date, timedelta
import calendar
import datetime

#função calcula dias antecedencia
def datas_ant(x):
    d = datetime.datetime.strptime(x, "%Y-%m-%d").date()  # converte string em data ou seja o x
    hj = date.today()
    diferenca = d - hj
    dias = diferenca.days
    return dias


@login_required
def mensagem(request):
    es = request.user.last_name
    hj = date.today()
    dd = date.today() + timedelta(days=30)#data de hoje mais 10
    data1 = request.GET.get('data1')
    data2 = request.GET.get('data2')
    permicao_escola_ninja = Escola.objects.filter(nome=es)
    for p in permicao_escola_ninja:
        per_n = p.permicao_mensagem
    if not data1 or  not data2:
        data1 = str(hj)
        data2 = str(dd)
    evento = Mensagem.objects.filter(escola=es, data__range=[data1, data2])  # consultar intervalos de data
    if request.method == "POST":
        form = MensagemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mensagem')
    else:
        form = MensagemForm(initial={'escola':es})
    return render(request,'meu/texto.html',{'form':form, 'eventos':evento, 'data_inicial':data1, 'data_final':data2, 'per_m':per_n})

@login_required()

def del_mensagem(request, id):
    tec = get_object_or_404(Mensagem, pk=id)
    if request.method == 'POST':
        tec.delete()
        return redirect('mensagem')
    return render(request, 'meu/del_tec.html',{'tec':tec})

@login_required
def home (request):
    hj = date.today()
    data = request.GET.get('data')
    tecnologia = request.GET.get('tecnologia')
    es = request.user.last_name
    if not data:
        data=str(hj)
    if not tecnologia:
        tecnologia=Aparelho.objects.filter(escola=es)[0]
    print(data)
    dd = date.today() + timedelta(days=3)  # data de hoje mais 10
    evento = Mensagem.objects.filter(escola=es, data__range=[hj, dd])
    x=datetime.datetime.strptime(data, '%Y-%m-%d').date()# converte string em data
    pesquisa =Agenda.objects.filter(data=data,eletronico=tecnologia).order_by('aula')
    aparelhos= Aparelho.objects.filter(escola=es)
    return render(request,'meu/home.html',{'dados':pesquisa,'data':data, 'tecnologia':tecnologia,'nomes':aparelhos,'hj':hj, 'x':x, 'evento':evento})

@login_required
def agenda_form(request, data, tecnologia):
    es = request.user.last_name
    di = Escola.objects.filter(nome=es)
    for  d in di:
        print(d.dias)
        print(d.permicao)
    antecedencia_aula = d.dias
    permicao_radio = d.permicao
    resultado = datas_ant(data)#função calcula datas
    if resultado > antecedencia_aula - 1:
        x = datetime.datetime.strptime(data, '%Y-%m-%d').date()  # converte string em data
        hj = date.today()#data hoje
        username = request.user.username
        escola = request.user.last_name
        form = AgendaForm(request.POST or None,initial={'nome':username,'data':data,'eletronico':tecnologia,'escola':escola ,'aula':'x'})
        nome_atual = request.POST.get('nome')
        print(nome_atual)
        tema = request.POST.get('tema')
        objetivo = request.POST.get('objetivo')
        m1 = request.POST.get('m1')
        m2 = request.POST.get('m2')
        m3 = request.POST.get('m3')
        m4 = request.POST.get('m4')
        m5 = request.POST.get('m5')
        m6 = request.POST.get('m6')
        v1 = request.POST.get('v1')
        v2 = request.POST.get('v2')
        v3 = request.POST.get('v3')
        v4 = request.POST.get('v4')
        v5 = request.POST.get('v5')
        v6 = request.POST.get('v6')
        n1 = request.POST.get('n1')
        n2 = request.POST.get('n2')
        n3 = request.POST.get('n3')
        n4 = request.POST.get('n4')
        n5 = request.POST.get('n5')
        #agendar todas as aulas
        if m1:
            try:
                ad1 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema, objetivo=objetivo,aula='am')
                ad1.save()
            except:
                messages.warning(request, '1ª aula do matutino indisponível!')
        if m2:
            try:
                ad2 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,objetivo=objetivo, aula='bm')
                ad2.save()
            except:
                messages.warning(request, '2ª aula do matutino indisponível!')
        if m3:
            try:
                ad3 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,objetivo=objetivo, aula='cm')
                ad3.save()
            except:
                messages.warning(request, '3ª aula do matutino indisponível!')
        if m4:
            try:
                ad4 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema, objetivo=objetivo,aula='dm')
                ad4.save()
            except:
                messages.warning(request, '4ª aula do matutino indisponível!')
        if m5:
            try:
                ad5 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema, objetivo=objetivo,aula='em')
                ad5.save()
            except:
                messages.warning(request, '5ª aula do matutino indisponível!')
        if m6:
            try:
                ad6 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema, objetivo=objetivo,aula='fm')
                ad6.save()
            except:
                messages.warning(request, '6ª aula do matutino indisponível!')


        if v1:
            try:
                ad7 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='gv')
                ad7.save()
            except:
                messages.warning(request, '1ª aula do vespertino indisponível!')
        if v2:
            try:
                ad8 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='hv')
                ad8.save()
            except:
                 messages.warning(request, '2ª aula do vespertino indisponível!')
        if v3:
            try:
                ad9 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='iv')
                ad9.save()
            except:
                messages.warning(request, '3ª aula do vespertino indisponível!')
        if v4:
            try:
                ad10 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='jv')
                ad10.save()
            except:
                messages.warning(request, '4ª aula do vespertino indisponível!')
        if v5:
            try:
                ad11 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='lv')
                ad11.save()
            except:
                messages.warning(request, '5ª aula do vespertino indisponível!')
        if v6:
            try:
                ad12 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='mv')
                ad12.save()
            except:
                messages.warning(request, '6ª aula do vespertino indisponível!')
        if n1:
            try:
                ad13 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='nn')
                ad13.save()
            except:
                messages.warning(request, '1ª aula do noturno indisponível!')
        if n2:
            try:
                ad14 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='on')
                ad14.save()
            except:
                 messages.warning(request, '2ª aula do noturno indisponível!')
        if n3:
            try:
                ad15 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='pn')
                ad15.save()
            except:
                messages.warning(request, '3ª aula do noturno indisponível!')
        if n4:
            try:
                ad16 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='qn')
                ad16.save()
            except:
                messages.warning(request, '4ª aula do noturno indisponível!')
        if n5:
            try:
                ad17 = Agenda(nome=nome_atual, data=data, eletronico=tecnologia, escola=escola, tema=tema,
                                 objetivo=objetivo, aula='rn')
                ad17.save()
            except:
                messages.warning(request, '5ª aula do noturno indisponível!')

        if form.is_valid():
                #form.save()
            pesquisa = Agenda.objects.filter(data=data, eletronico=tecnologia).order_by('aula')
            aparelhos = Aparelho.objects.filter(escola=es)
            return render(request,'meu/home.html',{'hj':hj,'dados':pesquisa,'data':data, 'tecnologia':tecnologia,'nomes':aparelhos,'x':x})
               # messages.warning(request, 'Está aula já foi agendada por outro usuário!')
        pesquisa = Agenda.objects.filter(data=data, eletronico=tecnologia, escola=es).order_by('aula')
        return render(request,'meu/agenda_form.html',{'form':form, 'data':data, 'tecnologia':tecnologia,'pes':pesquisa ,"permicao":permicao_radio})
    else:
        pesquisa = Agenda.objects.filter(data=data, eletronico=tecnologia)
        es = request.user.last_name
        aparelhos = Aparelho.objects.filter(escola=es)
        x = datetime.datetime.strptime(data, '%Y-%m-%d').date()  # converte string em data
        hj = date.today()
        dd=str(antecedencia_aula)
        messages.warning(request, 'Não é permitido agendar esta data! Você deve agendar com %s dia de antecedência(s).' % (dd,))
        return render(request, 'meu/home.html',{'hj': hj, 'dados': pesquisa, 'data': data, 'tecnologia': tecnologia, 'nomes': aparelhos, 'x': x})


@login_required
def add_user(request):
    es = request.user.last_name
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            #abaixo é necessario encriptar a senha comset_password
            s = form.save()
            s.set_password(s.password)
            s.save()
            return redirect('add_user')
    else:
        form = UserForm(initial={'last_name':es})
    es = request.user.last_name
    users = User.objects.filter(last_name=es)
    return render(request,'meu/add_user.html',{'form':form,'users':users})

@login_required
def add_tec(request):
    es = request.user.last_name
    tec = Aparelho.objects.filter(escola=es)
    if request.method == "POST":
        form = TecnologiasForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('add_tec')
    else:
        form = TecnologiasForm(initial={'escola':es})
    return render(request,'meu/cad_tecnologias.html',{'form':form, 'tec':tec})

@login_required
def agenda_delete(request,id, data, tecnologia):
    es = request.user.last_name
    agenda = get_object_or_404(Agenda, pk=id)
    hj = date.today()
    aparelhos = Aparelho.objects.filter(escola=es)
    x = datetime.datetime.strptime(data, '%Y-%m-%d').date()  # converte string em data
    pesquisa = Agenda.objects.filter(data=data, eletronico=tecnologia).order_by('aula')
    if request.method == 'POST':
        agenda.delete()
        return render(request, 'meu/home.html',{'dados':pesquisa, 'data': data,
        'tecnologia': tecnologia, 'nomes': aparelhos,'hj': hj, 'x': x})
    return render(request, 'meu/agenda_delete.html',{'agenda':agenda})

@login_required()

def del_tecnologia(request, id):
    tec = get_object_or_404(Aparelho, pk=id)
    if request.method == 'POST':
        tec.delete()
        return redirect('add_tec')
    return render(request, 'meu/del_tec.html',{'tec':tec})


def del_pessoa(request, id):
    pessoa = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('add_user')
    return render(request, 'meu/delete_user.html',{'pessoa':pessoa})

@login_required
def atualizar(request,id, data, tecnologia):
    es = request.user.last_name
    age = get_object_or_404(Agenda, pk=id)
    hj = date.today()
    aparelhos = Aparelho.objects.filter(escola=es)
    pesquisa = Agenda.objects.filter(data=data, eletronico=tecnologia).order_by('aula')
    x = datetime.datetime.strptime(data, '%Y-%m-%d').date()  # converte string em data

    form = AgendaForm(request.POST or None, instance=age)
    if form.is_valid():
        form.save()
        return render(request, 'meu/home.html', {'dados': pesquisa, 'data': data,
        'tecnologia': tecnologia, 'nomes': aparelhos, 'hj': hj, 'x': x})
    return render(request,'meu/atualizar.html',{'form':form})

@login_required
def pesquisa(request):
    hj = date.today()
    data = request.GET.get('data')
    if not data:
        data=str(hj)
    pesquisa = Agenda.objects.filter(data=data,escola=request.user.last_name).order_by('aula')
    return render(request,'meu/pesquisa.html',{'nomes':pesquisa, 'data':data, 'hj':hj})

@login_required
def tec_pesquisa(request):
    hj = date.today()
    es = request.user.last_name
    data = request.GET.get('data')
    if not data:
        data=str(hj)
    #tecnologia = request.GET.get('tecnologia')
    aparelhos = Aparelho.objects.filter(escola=es)
    return render(request,'meu/tecnologia.html',{'nomes':aparelhos,'data':data})
#logout
def sair_logout(request):
    logout(request)
    return render(request, 'meu/sair.html')
#painel contato
def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mensagem = form.cleaned_data['mensagem']
            email = form.cleaned_data['email']
            #print(nome,mensagem,email)
            send_mail('AgendaApp/Nome: {}, email do usuário: {}'.format(nome,email),'AgendaApp enviou uma mensagem: {}'.format(mensagem),'jorgescorpionsound@gmail.com',['jorgescorpionsound@hotmail.com'],fail_silently=False,)
            messages.info(request, 'Email enviado com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'meu/contato.html', {'form': form,'validade':True})

@login_required
#painel admin
def admin_sistema(request):
    return render(request, 'meu/admin.html')

def dias(request):
    es = request.user.last_name
    form = Escola.objects.filter(nome=es)
    return render(request, 'meu/cad_dias.html', {'form': form})

@login_required
def atualizar_dias(request,id):
    age = get_object_or_404(Escola, pk=id)
    form = EscolaForm(request.POST or None, instance=age)
    if form.is_valid():
        form.save()
        messages.info(request,'Dados salvos!')
        return render(request, 'meu/atualizar_dias.html', {'form':form})
    return render(request,'meu/atualizar_dias.html',{'form':form})


diasemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']


def dia_da_semana(mes, dia_da_semana):
    l = []
    dia = 1
    hj = date.today()
    quantos_dias_tem_um_mes = calendar.mdays[mes]
    for x in range(quantos_dias_tem_um_mes):

        data1 = datetime.date(day=dia, month=mes, year=hj.year)
        if diasemana[data1.weekday()] == dia_da_semana:
            # print('Mês: ',mes, dia, diasemana[data1.weekday()])
            #resultado = (hj.year, mes, dia)
            res = datetime.date(year=hj.year, month=mes,day=dia)
            l.append(res)
        dia += 1
    return l


@login_required
def add_ninja(request):
    #print(dia_da_semana(1,'Domingo'))
    es = request.user.last_name
    permicao_escola_ninja = Escola.objects.filter(nome=es)
    for p in permicao_escola_ninja:
        per_n=p.permicao_ninja
    nomes_tec = Aparelho.objects.filter(escola=es)
    tec = Aparelho.objects.filter(escola=es)[0]
    username = request.user.username
    form = AgendaForm(request.POST or None, initial={'nome': username, 'escola': es})
    if request.method == "POST":
        tema = request.POST.get('tema')
        nome = request.POST.get('nome')
        objetivo = request.POST.get('objetivo')
        tecnologia = request.POST.get('tecnologia')
        semana = request.POST.get('semana')
        aula = request.POST.get('aula')
        print(tema,objetivo,semana,aula,tecnologia)
        hj = date.today()
        mes_atual = hj.month
        try:
            for i in range(mes_atual, 13):  # percorre todos os meses de 1 a 12 sendo janeiro 1
                for i in dia_da_semana(i, semana):  # mes e dia da semana no caso 0 será segunda-feira
                    verifica = Agenda.objects.filter(escola=es,data=i,aula=aula)
                    if verifica:
                        verifica.delete()
                    a = Agenda(nome=nome, data=i, eletronico=tecnologia, escola=es, tema=tema,objetivo=objetivo, aula=aula)
                    a.save()

            messages.info(request, 'Aulas salvas com sucesso')
        except:
            messages.warning(request, 'Erros ao salvar!')
    else:
        form = AgendaForm(initial={'escola':es, 'nome':username, 'tema': 'Tema','objetivo':'Objetivo'})
    return render(request,'meu/ninja.html',{'form':form, 'nomes':nomes_tec, 'tecnologia':tec,'per_n':per_n})