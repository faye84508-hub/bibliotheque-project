import django_filters
from .models import Livre

class LivreFilter(django_filters.FilterSet):
    annee_min = django_filters.NumberFilter(field_name='annee_publication', lookup_expr='gte')
    annee_max = django_filters.NumberFilter(field_name='annee_publication', lookup_expr='lte')

    class Meta:
        model = Livre
        fields = ['categorie', 'disponible']