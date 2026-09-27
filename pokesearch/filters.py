import django_filters
from django.db.models import Q

from pokesearch.models import Pokemon


class PokemonFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(method='filter_type', label='Type (matches either slot)')
    generation = django_filters.NumberFilter(field_name='generation')

    class Meta:
        model = Pokemon
        fields = ['type', 'generation']

    def filter_type(self, queryset, name, value):
        return queryset.filter(
            Q(type1__name__iexact=value) | Q(type2__name__iexact=value)
        )
