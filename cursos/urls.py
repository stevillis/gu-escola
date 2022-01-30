from django.urls import path

from cursos.views import AvaliacaoAPIView, CursoAPIView

urlpatterns = [
    path("cursos/", CursoAPIView.as_view(), name="cursos"),
    path("avaliacoes/", AvaliacaoAPIView.as_view(), name="avaliacoes"),
]
