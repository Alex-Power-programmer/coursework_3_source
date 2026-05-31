FROM python:3.10-slim

WORKDIR /project

COPY requirements.txt .
COPY requirements.dev.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "127.0.0.0:25000", "app:create_app()"]


