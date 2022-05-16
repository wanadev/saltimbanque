FROM debian:11

RUN apt update \
	&& apt install -y \
		nginx \
		python3-pip \
		python3-venv \
		supervisor \
# Saltimbanque dependencies
		libcairo2 \
		libpango1.0-0 \
		fonts-roboto \
	&& rm -rf \
		/var/cache/apt \
		/var/log/nginx/access.log \
		/var/log/nginx/error.log \
	&& ln -s /dev/stdout /var/log/nginx/access.log \
	&& ln -s /dev/stderr /var/log/nginx/error.log

# Supervisor
COPY ./docker/prod/supervisor/supervisord.conf /etc/supervisor/
COPY ./docker/prod/supervisor/gunicorn.conf /etc/supervisor/conf.d/
COPY ./docker/prod/supervisor/nginx.conf /etc/supervisor/conf.d/

# NGinx
EXPOSE 80

COPY ./docker/prod/nginx/default.conf /etc/nginx/sites-enabled/default

# Saltimbanque
WORKDIR /saltimbanque

COPY . /saltimbanque

RUN python3 -m venv __env__ \
	&& bash -c "source __env__/bin/activate && pip install --upgrade pip" \
	&& bash -c "source __env__/bin/activate && pip install -r requirements.txt gunicorn"

CMD ["supervisord", "--nodaemon"]
