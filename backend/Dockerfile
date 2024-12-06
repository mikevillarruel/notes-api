FROM python:3.10 AS base

WORKDIR /project

COPY .  /project
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

EXPOSE 8000


FROM base AS dev

ENTRYPOINT ["fastapi", "dev", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM base AS prod

ENTRYPOINT ["fastapi", "run"]
