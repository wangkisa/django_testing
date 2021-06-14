# pull official base image
# FROM python:3.6.4
FROM ubuntu:16.04

ARG DEBIAN_FRONTEND=noninteractive
# Configure python
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 TZ=Asia/Seoul

# Install libmysqlclient for Django
# RUN apt-get update && apt-get install -y python-dev gcc openjdk-9-jdk

RUN apt-get update && \
        apt-get install -y tzdata && \
        apt-get install -y software-properties-common && \
        add-apt-repository -y ppa:fkrull/deadsnakes && \
        apt-get update -y  && \
        apt-get install -y build-essential python3.6 python3.6-dev python3-pip && \
#         apt-get install -y git  && \
        # update pip
        python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel && \
        apt-get -o Dpkg::Options::="--force-overwrite" install -y openjdk-9-jdk
#         apt-get install -y openjdk-9-jdk

# Install entr from the source. It should be patched to watch files in docker container.
# https://bitbucket.org/eradman/entr/issues/42/changes-to-files-in-docker-volumes-arent#comment-46788220
# RUN wget http://eradman.com/entrproject/code/entr-3.9.tar.gz \
#     && tar zvxf entr-3.9.tar.gz \
#     && cd eradman-entr-332fd96a324a \
#     && wget http://entrproject.org/patches/entr-3.9-wsl \
#     && patch -p1 < entr-3.9-wsl \
#     && ./configure \
#     && make install

WORKDIR /app
COPY ./ ./

# COPY docker_requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# COPY ./ ./
