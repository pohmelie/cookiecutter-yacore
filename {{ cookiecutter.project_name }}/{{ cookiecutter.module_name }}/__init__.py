from importlib import resources

__version__ = resources.read_text("{{ cookiecutter.module_name }}", "version.txt").strip()
version = tuple(map(int, __version__.split(".")))
