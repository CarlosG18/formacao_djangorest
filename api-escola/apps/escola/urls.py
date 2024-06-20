from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', views.AlunoViewSet, basename='alunos')
router.register('cursos', views.CursoViewSet, basename='cursos')

app_name = 'escola'
urlpatterns = [
    path('', include(router.urls)),
]
