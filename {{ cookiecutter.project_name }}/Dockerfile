FROM python:{{ cookiecutter.python_version }}-slim as builder

WORKDIR /{{ cookiecutter.project_name }}
RUN apt update && apt install -y build-essential
RUN python -m venv env
COPY requirements/production.txt requirements/production.txt
RUN env/bin/python -m pip install -r requirements/production.txt


FROM python:{{ cookiecutter.python_version }}-slim as runner

COPY --from=builder /{{ cookiecutter.project_name }} /{{ cookiecutter.project_name }}
WORKDIR /{{ cookiecutter.project_name }}
COPY ./ ./
RUN env/bin/python -m pip install -e ./

CMD ["env/bin/python", "-m", "{{ cookiecutter.module_name }}"]
