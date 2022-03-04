import re

from drf_spectacular.utils import extend_schema, OpenApiParameter

from drfSpectecularReproducer.models import Resource

ADDITIONAL_PARAMETERS = {
    "resource_name": OpenApiParameter(
        "r_name", str, location=OpenApiParameter.PATH,
        description=Resource._meta.get_field("name").help_text
    ),
}


def annotate_parameters(endpoints):
    new_endpoints = []
    for (path, path_regex, method, callback) in endpoints:
        path_parameters = re.findall(r"\{(.*?)\}", path)
        replacable_parameters = set(path_parameters) & set(ADDITIONAL_PARAMETERS.keys())
        if replacable_parameters:
            for path_parameter in replacable_parameters:
                path = path.replace("{" + path_parameter + "}", "{" + ADDITIONAL_PARAMETERS[path_parameter].name + "}")
            extend_decorator = extend_schema(
                parameters=[ADDITIONAL_PARAMETERS[path_parameter] for path_parameter in replacable_parameters]
            )
            # Do the following a few times in a loop to trigger max recursion depth earlier
            for i in range(10):
                callback.cls = extend_decorator(callback.cls)
        new_endpoints.append((path, path_regex, method, callback))
    return new_endpoints
