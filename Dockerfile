FROM python:3.10-alpine
WORKDIR /app
EXPOSE 8888
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt
COPY templates templates
COPY main.py .
ENTRYPOINT ["python3", "main.py"]
