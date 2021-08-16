import django_filters as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug')
    category = filters.CharFilter(
        field_name='category__slug')
    name = filters.CharFilter(
        field_name='name', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ['year']