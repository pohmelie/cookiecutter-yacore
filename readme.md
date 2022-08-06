# cookiecutter-yacore
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for [yacore](https://github.com/pohmelie/yacore)-based project.

## Features
- main package with entrypoint and service skeleton
- requirements (dev/prod)
- tests configuration
- github actions for linter and tests
- setup.py
- dockerfile

## Usage
Deploy template and answer configurator questions.
```bash
pip install cookiecutter
cookiecutter gh:pohmelie/cookiecutter-yacore
```
Add extra dependencies to `requirements/production.in` and `requirements/dev.txt`. Compile `.in` dependencies to pin them.
```bash
cd your-project-name
pip install pip-tools
pii-compile requirements/production.in -o requirements/production.txt
```
Now you can install the app.
```bash
pip install -e ./[dev]
```
Run the tests.
```
pytest
```
Or build the docker image.
```bash
docker build . -t my-app
```
