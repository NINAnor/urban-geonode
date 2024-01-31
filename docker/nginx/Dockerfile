ARG BASE_IMAGE_VERSION
FROM geonode/nginx:${BASE_IMAGE_VERSION}

COPY ./geonode.conf.envsubst sites-enabled/
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
