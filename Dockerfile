FROM python:3.10.12-slim
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 3001
CMD ["python", "app.py"]