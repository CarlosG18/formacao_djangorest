from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import CursoSerializer, AlunoSerializer
from .models import Curso, Aluno

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Create your views here.
def alunos(request):
    if request.method == 'GET':
        alunos = {
            'id': 1,
            'nome': 'carlos',
        }
        return JsonResponse(alunos)