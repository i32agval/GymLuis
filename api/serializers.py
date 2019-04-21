from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Get information of users in the API
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
