FROM python:3.13.3-alpine3.22

# Установка Allure
RUN apk update && \
    apk add --no-cache \
    openjdk11-jre \
    curl \
    tar && \
    curl -o allure-2.24.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz && \
    tar -zxvf allure-2.24.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure && \
    rm allure-2.24.0.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt