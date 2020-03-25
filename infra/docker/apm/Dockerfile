FROM docker.elastic.co/apm/apm-server:7.0.0
RUN mkdir -p /usr/share/apm-server
COPY ./apm-server.yml /usr/share/apm-server/apm-server.yml
USER root
RUN chown apm-server /usr/share/apm-server/apm-server.yml
USER apm-server