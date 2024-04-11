FROM python:3-slim

WORKDIR /app

COPY . /app

# Instalar dependencias y limpiar archivos innecesarios
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip && \
    pip3 install --no-cache-dir flask flask_socketio gevent-websocket && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=8080

EXPOSE 8080

CMD ["python3", "application.py"]
