FROM python:3-alpine
LABEL maintainer="auth_fastapi_app"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./src/web /src/web

WORKDIR /src/web
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install psycopg2-binary

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt 

ENV PATH="/py/bin:$PATH"

EXPOSE 8000

CMD ["python", "manage.py"]