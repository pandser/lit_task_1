from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    image = Base64ImageField()