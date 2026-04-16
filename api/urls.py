from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreViewSet, TagViewSet  # ✅ AJOUT
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .views import ProfilView, ajouter_favori

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('auteurs', AuteurViewSet)
router.register('livres', LivreViewSet)
router.register('tags', TagViewSet)  # ✅ maintenant reconnu

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
@action(detail=True, methods=['post'])
def emprunter(self, request, pk=None):
    livre = self.get_object()

    if not livre.disponible:
        return Response(
            {"erreur": "Livre non disponible"},
            status=status.HTTP_400_BAD_REQUEST
        )

    livre.disponible = False
    livre.save()

    return Response({"message": f"{livre.titre} emprunté"})
urlpatterns += [
    path('profil/', ProfilView.as_view()),
    path('profil/favoris/', ajouter_favori),
]