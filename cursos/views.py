from rest_framework.generics import ListCreateAPIView

from cursos.models import Curso, Avaliacao
from cursos.serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
