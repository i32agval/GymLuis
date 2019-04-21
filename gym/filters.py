import django_filters

from .models import UserProfile


class UserProfileFilter(django_filters.FilterSet):
    """
    class to filter users
    """
    user__first_name = django_filters.CharFilter(
        lookup_expr='icontains', label="Nombre")
    user__last_name = django_filters.CharFilter(
        lookup_expr='icontains', label="Apellidos")
    city = django_filters.CharFilter(
        lookup_expr='icontains', label="Ciudad")

    class Meta:
        model = UserProfile
        fields = ['user__first_name', 'user__last_name', 'city']
