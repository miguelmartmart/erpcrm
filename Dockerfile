# Usar la imagen oficial de Python 3.12
FROM python:3.12-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    git \
    libldap2-dev \
    libsasl2-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear y establecer el directorio de trabajo
WORKDIR /opt/odoo

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto de Odoo
EXPOSE 8069

# Comando para ejecutar Odoo
CMD ["/opt/odoo/odoo-bin", "-c", "/opt/odoo/.odoorc"]
