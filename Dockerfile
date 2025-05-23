FROM python:3.8

# Install pkg-config and MySQL development headers
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Now install your Python requirements
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
