# Usa una imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /twitter_detector

# Copia los archivos de tu proyecto al contenedor
COPY . /twitter_detector

# Instala las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto que Flask utilizará (por defecto 5000)
EXPOSE 5000

# Define el comando para ejecutar tu aplicación Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]