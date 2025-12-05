FROM python:3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt /app/
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /app/