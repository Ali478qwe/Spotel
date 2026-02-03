FROM python:3.13.9

RUN apt-get update && aptt-get install -y \ ffmpeg \ && rm -rf /var/lib/lists/*

WORKDIR /Src

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","main.py"]