from django.db import models


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    payload = models.TextField()
    name = models.CharField(max_length=100, unique=True, help_text="Name of resource")


class NestedResource(models.Model):
    id = models.AutoField(primary_key=True)
    nested_payload = models.TextField()
    related_resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

