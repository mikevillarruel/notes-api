FROM python:3.10

WORKDIR /project

COPY .  /project

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

EXPOSE 8080

CMD python /project/runner.py
