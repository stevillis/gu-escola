from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.response import Response

from cursos.models import Avaliacao, Curso
from cursos.serializers import AvaliacaoSerializer, CursoSerializer

"""
API v1
"""


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


"""
API v2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        print(request)
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


class AvaliacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
