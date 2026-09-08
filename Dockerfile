FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

ENV DB_PATH=/data/todo.db
VOLUME ["/data"]
EXPOSE 5000

CMD ["python", "-m", "app.main"]
