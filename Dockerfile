FROM python:3.13.3-alpine3.22

# Установка Allure
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless curl tar && \
    curl -o allure-2.24.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz && \
    tar -zxvf allure-2.24.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure && \
    rm allure-2.24.0.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt