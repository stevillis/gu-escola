from rest_framework import serializers

from cursos.models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes')
