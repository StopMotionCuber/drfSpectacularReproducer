from rest_framework import viewsets, permissions

from drfSpectecularReproducer.models import Resource, NestedResource
from drfSpectecularReproducer.serializers import ResourceSerializer, NestedResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    """
    Interact with Storage Manager properties
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Resource.objects.all()
    lookup_field = "name"


class NestedResourceViewSet(viewsets.ModelViewSet):
    """
    Interact with File System properties
    """
    serializer_class = NestedResourceSerializer
    permission_classes = [permissions.AllowAny]
    queryset = NestedResource.objects.all()

    def get_queryset(self):
        return NestedResource.objects.filter(
            related_resource__name=self.kwargs["resource_name"]
        )
