from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Auteur, Livre, Tag
from .serializers import AuteurSerializer, LivreSerializer, TagSerializer
from .permissions import EstProprietaireOuReadOnly
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

from .models import ProfilLecteur, Livre
from .serializers import ProfilLecteurSerializer
from rest_framework.response import Response

@api_view(['GET'])
def liste_favoris(request):
    profil, _ = ProfilLecteur.objects.get_or_create(user=request.user)
    livres = profil.livres_favoris.all()
    serializer = LivreSerializer(livres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouter_favori(request):
    profil, created = ProfilLecteur.objects.get_or_create(user=request.user)

    livre_id = request.data.get('livre_id')
    livre = Livre.objects.get(id=livre_id)

    profil.livres_favoris.add(livre)

    return Response({"message": "Livre ajouté aux favoris"})


# ✅ PROFIL
class ProfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profil, created = ProfilLecteur.objects.get_or_create(user=request.user)
        serializer = ProfilLecteurSerializer(profil)
        return Response(serializer.data)

    def put(self, request):
        profil, created = ProfilLecteur.objects.get_or_create(user=request.user)
        serializer = ProfilLecteurSerializer(profil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "erreur": "Données de profil invalides",
            "details": serializer.errors
        }, status=400)





# ✅ AUTEUR
class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer


# ✅ LIVRE
class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [EstProprietaireOuReadOnly]

    @action(detail=True, methods=['post'])
    def emprunter(self, request, pk=None):
        livre = self.get_object()
        if not livre:
            return Response({"erreur": "Livre non trouvé"}, status=404)
        if not livre.disponible:
            return Response({
                "erreur": "Livre non disponible",
                "details": f"{livre.titre} est déjà emprunté."
            }, status=400)

        livre.disponible = False
        livre.save()

        return Response({"message": f"Livre '{livre.titre}' emprunté avec succès"})


# ✅ TAG
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer