from facet import ServiceMixin
from yacore.injector import inject, register


class {{ cookiecutter.service_class_name }}(ServiceMixin):

    def __init__(self):
        pass

    @property
    def dependencies(self):
        return []

    async def start(self):
        pass

    async def stop(self):
        pass


@register(name="{{ cookiecutter.module_name }}", singleton=True)
@inject
def {{ cookiecutter.module_name }}_from_config(config):
    return {{ cookiecutter.service_class_name }}()
