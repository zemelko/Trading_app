FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Необходимо дать пользователю доступ для запуска bash скриптов
RUN chmod a+x docker/*.sh
