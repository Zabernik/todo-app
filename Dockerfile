# Użycie obrazu Python
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie pliku requirements.txt do katalogu roboczego
COPY requirements.txt /app/

# Instalacja zależności
RUN pip install -r requirements.txt

# Kopiowanie całej aplikacji
COPY app /app

# Otwarcie portu 5000
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "app.py"]
