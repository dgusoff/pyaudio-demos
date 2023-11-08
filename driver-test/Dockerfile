FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# Install package dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        alsa-base \
        alsa-utils \
        libsndfile1-dev && \
    apt-get clean

COPY audiotest.sh app/audiotest.sh

WORKDIR /app

RUN ls 
RUN arecord -l
RUN chmod +x audiotest.sh
RUN ./audiotest.sh
ENTRYPOINT [ "./audiotest.sh" ]