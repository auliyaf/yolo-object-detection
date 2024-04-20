FROM python:3.10.12-slim
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y gcc
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python", "app.py"]
