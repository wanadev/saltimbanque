FROM python:3

COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint

RUN chmod +x /usr/local/bin/docker-entrypoint

WORKDIR /app

ENTRYPOINT ["docker-entrypoint"]
CMD ["flask", "run", "--host=0.0.0.0"]