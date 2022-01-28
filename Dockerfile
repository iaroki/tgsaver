FROM python:3.10-alpine
WORKDIR /app
EXPOSE 8888
COPY requirements.txt /app/
RUN pip install --no-cache -r requirements.txt
COPY templates /app/
COPY main.py /app/
ENTRYPOINT ["python3", "main.py"]
