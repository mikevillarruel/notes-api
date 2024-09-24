FROM python:3.10

WORKDIR /project

COPY .  /project

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

EXPOSE 8000

ENTRYPOINT ["fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]
