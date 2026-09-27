from rest_framework import serializers

from pokesearch.models import Pokemon, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class PokemonSerializer(serializers.ModelSerializer):
    type1 = TypeSerializer(read_only=True)
    type2 = TypeSerializer(read_only=True)
    type1_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type1', write_only=True, allow_null=True, required=False
    )
    type2_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type2', write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'generation', 'type1', 'type2', 'type1_id', 'type2_id']
