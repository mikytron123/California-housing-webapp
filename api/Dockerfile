# syntax = docker/dockerfile:1.4-labs
#
# ===========================================
#
# THIS IS A GENERATED DOCKERFILE. DO NOT EDIT
#
# ===========================================

# Block SETUP_BENTO_BASE_IMAGE
FROM python:3.8-slim

ENV LANG=C.UTF-8

ENV LC_ALL=C.UTF-8

ENV PYTHONIOENCODING=UTF-8

ENV PYTHONUNBUFFERED=1


USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,target=/var/lib/apt \ 
    --mount=type=cache,target=/var/cache/apt \
	apt-get update -y \
    && apt-get install -q -y --no-install-recommends --allow-remove-essential \
		ca-certificates gnupg2 bash build-essential


# Block SETUP_BENTO_USER
ARG BENTO_USER=bentoml
ARG BENTO_USER_UID=1034
ARG BENTO_USER_GID=1034
RUN groupadd -g $BENTO_USER_GID -o $BENTO_USER && useradd -m -u $BENTO_USER_UID -g $BENTO_USER_GID -o -r $BENTO_USER
SHELL [ "/bin/bash", "-eo", "pipefail", "-c" ]
ARG BENTO_PATH=/home/bentoml/bento
ENV BENTO_PATH=$BENTO_PATH
ENV BENTOML_HOME=/home/bentoml/

RUN mkdir $BENTO_PATH && chown bentoml:bentoml $BENTO_PATH -R
WORKDIR $BENTO_PATH

# init related components
COPY --chown=bentoml:bentoml . ./



# Block SETUP_BENTO_COMPONENTS

# Running install.sh to install python packages
RUN --mount=type=cache,target=/root/.cache/pip bash <<EOF
set -euxo pipefail

if [ -f /home/bentoml/bento/env/python/install.sh ]; then
  echo "install.sh to install python packages..."
  chmod +x /home/bentoml/bento/env/python/install.sh
  /home/bentoml/bento/env/python/install.sh
fi
EOF

# Running user setup scripts
RUN  bash <<EOF
set -euxo pipefail

if [ -f /home/bentoml/bento/env/docker/setup_script ]; then
  echo "user setup scripts..."
  chmod +x /home/bentoml/bento/env/docker/setup_script
  /home/bentoml/bento/env/docker/setup_script
fi
EOF


# Block SETUP_BENTO_ENTRYPOINT
RUN rm -rf /var/lib/{apt,cache,log}
# Default port for BentoServer
EXPOSE 3000

RUN chmod +x /home/bentoml/bento/env/docker/entrypoint.sh

USER bentoml

ENTRYPOINT [ "/home/bentoml/bento/env/docker/entrypoint.sh" ]

CMD [ "bentoml", "serve", "/home/bentoml/bento", "--production" ]

