# Utiliza una imagen base ligera de Python
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

# Directorio de trabajo
WORKDIR $APP_HOME

# Copia y instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto de la API
EXPOSE 8000

# Comando de arranque de la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]