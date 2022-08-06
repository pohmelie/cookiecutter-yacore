# {{ cookiecutter.project_name }}

## Requirements
- python {{ cookiecutter.python_version }}
- docker

## Installation
``` shell
pip install pip-tools
pip-compile requirements/production.in -o requirements/production.txt
pip install -e ./[dev]
```

## Testing
``` shell
pytest
```
