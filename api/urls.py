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
urlpatterns += [
    path('profil/', ProfilView.as_view()),
    path('profil/favoris/', ajouter_favori),
]