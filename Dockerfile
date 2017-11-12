FROM python:3.6

ADD requirements.txt /req.txt
WORKDIR /

RUN pip install -r req.txt

ADD ./src /app
WORKDIR /app

CMD ["python", "core.py"]
