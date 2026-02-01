FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY . /app
RUN ls -la /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "data_manager.py"]