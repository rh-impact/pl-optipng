# Docker file for optipng ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-optipng .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-optipng .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-optipng
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-optipng
#

FROM python:3.10-slim-bullseye
LABEL maintainer="rh-impact <porridge@redhat.com>"

WORKDIR /usr/local/src

RUN apt-get update && \
    apt-get install -y optipng && \
    apt-get clean && \
    find /var/lib/apt/lists/ -type f -not -name lock -delete

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["optipng", "--help"]
