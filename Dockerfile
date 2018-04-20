FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["./startup.sh"]