from rest_framework import serializers
from .models import Auteur, Livre, Tag, ProfilLecteur


class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProfilLecteurSerializer(serializers.ModelSerializer):
    livres_favoris = LivreSerializer(many=True, read_only=True)

    livre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Livre.objects.all(),
        source='livres_favoris',
        write_only=True,
        required=False
    )

    class Meta:
        model = ProfilLecteur
        fields = [
            'id',
            'adresse',
            'telephone',
            'date_naissance',
            'livres_favoris',
            'livre_ids'
        ]