import asyncio

from cock import build_entrypoint
from yacore.injector import register

from {{ cookiecutter.module_name }} import __version__
from {{ cookiecutter.module_name }}.service import {{ cookiecutter.service_class_name }}


async def amain():
    await {{ cookiecutter.service_class_name }}().run()


def main(config):
    register(lambda: config, singleton=True, name="config")
    register(lambda: __version__, singleton=True, name="version")
    asyncio.run(amain())


options = []
entrypoint = build_entrypoint(main, options, auto_envvar_prefix="{{ cookiecutter.env_prefix }}_SERVICE", show_default=True)
if __name__ == "__main__":
    entrypoint(prog_name="{{ cookiecutter.project_name }}-service")
