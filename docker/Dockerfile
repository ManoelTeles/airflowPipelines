# VERSION 0.0.1
# AUTHOR: Manoel Teles
# DESCRIPTION: Basic Airflow container
# BUILD: 
# SOURCE: 

  # Airflow Image
FROM debian:stretch-slim

  # configs
ENV AIRFLOW_HOME /home/airflow

ENV PACKAGES="\
  apt-transport-https \
  apt-utils \
  software-properties-common \
  bzip2 \
  kmod \
  iptables \
  net-tools \
  iputils-ping \
  dante-server \
  iproute2 \
  curl \
  dumb-init \
  musl \
  ca-certificates \
  git \
  python \
  python-dev \
  python-pip \
  python3 \
  python3-dev \
  python3-pip \
  sqlite3 \
  libsqlite3-dev \
  gcc \
  musl-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev \
  bash \
  unixodbc-dev \
  wget \
  libstdc++5:i386 \
  libx11-6:i386 \
  libpam0g:i386 \
  expect \
"

  #  install packages debian
RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -yq install $PACKAGES && \
    apt-get -y update 

  # Set Up Python
RUN echo -e "##################### set python3 as default #####################" && \
    echo '# set python3 as default' >> ~/.bashrc && \
    echo 'alias python=python3' >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc"

  # Create airflow dir 
RUN mkdir $AIRFLOW_HOME && \
    chmod 777 $AIRFLOW_HOME && \
    cd $AIRFLOW_HOME && \
    adduser --disabled-password --gecos "" airflow

  # install packges
RUN python3 -m pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install apache-airflow==1.9 && \
    pip install psycopg2-binary && \
    pip install pandas && \
    pip install numpy && \
    pip install pyodbc && \
    pip install pandas_gbq && \
    pip install flask_bcrypt && \
    pip install sqlalchemy==1.1.15
