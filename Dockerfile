FROM python:3.12

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]
