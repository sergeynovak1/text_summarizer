from rest_framework import serializers


class MethodSerializer(serializers.Serializer):
    text = serializers.CharField()