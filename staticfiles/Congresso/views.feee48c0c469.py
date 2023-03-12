from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from Congresso.models import Cursos, Frequencia
from Congresso.forms import FrequenciaForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def docad(request):
    # Realizar Cadastro
    data = {}

    if request.method == 'POST':
        if request.POST['usuario'] is None:
            data['msg'] = 'Campo Usuário Vazio'
            return render(request,'cadastro.html', data)
        
        if request.POST['usuario'] == '':
            data['msg'] = 'Campo Usuário Vazio'
            return render(request,'cadastro.html', data)
        
        if request.POST['senha'] == '':
            data['msg'] = 'Campo Senha Vazio'
            return render(request,'cadastro.html', data)
        
        if request.POST['senha'] is None:
            data['msg'] = 'Campo Senha Vazio'
            return render(request,'cadastro.html', data)
        
        if request.POST['senha'] == '':
            data['msg'] = 'Campo Senha Vazio'
            return render(request,'cadastro.html', data)
        
        testes = User.objects.filter(username=request.POST['usuario'])
    
        if testes:
            data['msg'] = 'Usuário Já Existe no BD!'
            return render(request,'cadastro.html', data)

        user = User.objects.create_user(username=request.POST['usuario'], password=request.POST['senha'])
        user.first_name = request.POST['usuario']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso!'
        return render(request,'cadastro.html', data)

    return render(request,'cadastro.html', data)

def dologin(request):
    data = {}
    if request.method == 'POST':
        user = request.POST['usuario']
        password = request.POST['senha']
        auth = authenticate(username=user, password=password)
    if auth is not None:
        login_django(request, auth)
        return redirect('inscritos')
    else:
        data['msg'] = 'Usuário ou Senha Incorreta!'
        return render(request, 'login.html', data)

def inscritos(request):
    return render(request, 'inscritos.html')

@login_required(redirect_field_name='login')
def confirm(request):
        form = FrequenciaForm()
        curso = Cursos.objects.get(curso='Evento Especial - Congresso da Liga')
        print(curso.curso)
        msg = curso.curso
        return render(request, 'qrcode.html', {'form':form, 'msg':msg})

def doconfirm(request):
    curso = Cursos.objects.get(id=1)
    checked = True
    data = {}
    if request.method == 'POST':
        frequencia = FrequenciaForm()
        frequencia = frequencia.save(commit=False)
        frequencia.aluno = request.user.id
        frequencia.cursoparticipado_id = curso.id
        frequencia.confirma = checked
        data['msg'] = 1
        frequencia = frequencia.save()
        return render(request, 'inscritos.html', data)
    else:
         frequencia = FrequenciaForm()

    return render(request, 'qrcode.html', {'frequencia': frequencia})

def congresso(request):
    return render(request, 'congresso.html')
