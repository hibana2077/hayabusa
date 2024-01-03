FROM python:3.10.0

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    htop \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

USER root

RUN mkdir -p /data

RUN chmod 777 /data

USER user

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -U pip

RUN pip3 install -r requirements.txt

COPY --chown=user ./src /app

EXPOSE 7860

CMD ["streamlit", "run", "main.py", "--server.port", "7860"]