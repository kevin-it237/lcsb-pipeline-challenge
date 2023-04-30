FROM python:3.8-slim-buster

COPY requirements.txt .
# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "pipeline.py"]
