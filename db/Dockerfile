ARG MYSQL_VERSION=8.0

FROM mysql:${MYSQL_VERSION}

ENV MYSQL_DATABASE=posterr

COPY ./scripts /docker-entrypoint-initdb.d/

RUN groupadd -r posterr && useradd --no-log-init -r -g posterr posterr_service && chown -R posterr_service:posterr /docker-entrypoint-initdb.d/

USER posterr_service
