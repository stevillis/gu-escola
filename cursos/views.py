from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)

from cursos.models import Avaliacao, Curso
from cursos.serializers import AvaliacaoSerializer, CursoSerializer


class CursosAPIView(ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        curso_pk = self.kwargs.get('curso_pk')
        if curso_pk:
            return self.queryset.filter(curso_id=curso_pk)
        return self.queryset.all()


class AvaliacaoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        curso_pk = self.kwargs.get('curso_pk')
        avaliacao_pk = self.kwargs.get('avaliacao_pk')
        if curso_pk:
            return get_object_or_404(self.get_queryset(), curso_id=curso_pk, pk=avaliacao_pk)
        return get_object_or_404(self.get_queryset(), pk=avaliacao_pk)
