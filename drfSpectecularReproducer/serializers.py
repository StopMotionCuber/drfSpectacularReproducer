from rest_framework import serializers

from drfSpectecularReproducer.models import Resource, NestedResource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ["name", "payload"]


class NestedResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedResource
        fields = ["nested_payload"]
