from rest_framework.response import Response
from rest_framework.views import APIView

from cursos.models import Avaliacao, Curso
from cursos.serializers import AvaliacaoSerializer, CursoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliacoes
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
