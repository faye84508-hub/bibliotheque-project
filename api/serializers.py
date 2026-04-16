from rest_framework import serializers
from .models import Auteur, Livre, Tag, ProfilLecteur


class AuteurSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(
        error_messages={
            'required': 'Le nom est obligatoire.',
            'blank': 'Le nom ne peut pas être vide.'
        }
    )

    class Meta:
        model = Auteur
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    titre = serializers.CharField(
        error_messages={
            'required': 'Le titre est obligatoire.',
            'blank': 'Le titre ne peut pas être vide.'
        }
    )

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

    adresse = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'L\'adresse est obligatoire.',
            'blank': 'L\'adresse ne peut pas être vide.',
            'max_length': 'L\'adresse est trop longue.'
        }
    )

    telephone = serializers.CharField(
        max_length=15,
        error_messages={
            'required': 'Le téléphone est obligatoire.',
            'blank': 'Le téléphone ne peut pas être vide.',
            'max_length': 'Le téléphone est trop long.'
        }
    )

    date_naissance = serializers.DateField(
        error_messages={
            'required': 'La date de naissance est obligatoire.',
            'invalid': 'Format de date invalide (AAAA-MM-JJ).'
        }
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
