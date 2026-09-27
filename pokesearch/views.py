from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from pokesearch.filters import PokemonFilter
from pokesearch.models import Pokemon, Type
from pokesearch.serializers import PokemonSerializer, TypeSerializer


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all().order_by('name')
    serializer_class = TypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.select_related('type1', 'type2').order_by('name')
    serializer_class = PokemonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PokemonFilter
    search_fields = ['name']
