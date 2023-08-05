ARG MYSQL_VERSION=8.0

FROM mysql:${MYSQL_VERSION}

ENV MYSQL_DATABASE=posterr

RUN groupadd -r posterr && useradd --no-log-init -r -g posterr_api posterr_service

COPY --chown=posterr:posterr_api ./scripts /docker-entrypoint-initdb.d/

USER posterr_api
