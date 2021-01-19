FROM python:3.6-stretch

WORKDIR /bakerista_backend

# sets the environment variable
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/bakerista_backend \
    DJANGO_SETTINGS_MODULE=bakerista_backend.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

EXPOSE 8000

# Install operating system dependencies.
RUN apt-get update -y && \
    apt-get install -y apt-transport-https rsync gettext libgettextpo-dev && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs &&\
    rm -rf /var/lib/apt/lists/*

# Install Gunicorn.
RUN pip install "gunicorn>=19.8,<19.9"

# start to install backend-end stuff
WORKDIR /bakerista_backend

# Install Python requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code.
COPY . .

# Install assets
RUN python manage.py collectstatic --noinput --clear

# Run application
CMD gunicorn config.wsgi:bakerista_backend