from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100, required=True)