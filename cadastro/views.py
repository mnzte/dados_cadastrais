from django.shortcuts import render, get_object_or_404
from .models import Alunos 

def index(request):
    alunos = Alunos.objects.all()
    return render (request, 'index.html',{'alunos':alunos})

def aluno(request, id ):
    aluno = get_object_or_404(Alunos, id=id)
    return render (request, 'aluno.html',{'aluno':aluno})


