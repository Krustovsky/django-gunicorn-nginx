FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY entrypoint.sh entrypoint.sh

RUN chmod +x /opt/app/entrypoint.sh

COPY . .
ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"]