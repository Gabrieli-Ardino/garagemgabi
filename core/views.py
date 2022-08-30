from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Marca, Carro
from core.serializers import CategoriaSerializer, CarroSerializer, MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    