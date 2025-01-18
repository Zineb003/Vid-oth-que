FROM python:3.9-slim

WORKDIR /app

# Installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1
CMD ["python", "-u", "app.py"]
