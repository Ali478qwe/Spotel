# FROM python:3.13-slim

# RUN apt-get update && apt-get install -y \
#     ffmpeg \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /Src

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

# COPY Src/ .

# CMD ["python", "main.py"]