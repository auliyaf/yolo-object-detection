FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["python", "app.py"]
