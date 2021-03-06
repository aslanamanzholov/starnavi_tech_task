FROM python:3.8.0-alpine3.10

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

COPY ./src /src
WORKDIR /src
# Add alpine mirrors
RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g' \
    /etc/apk/repositories && \
# Set timezone
    apk add tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime && \
    echo "Asia/Almaty" > /etc/timezone && apk del tzdata && \
# Add system dependencies
    apk update && \
    apk add bash postgresql-client \
    gcc musl-dev postgresql-dev gettext && \
# Upgrade pip
    pip install --upgrade pip && \
# Add project dependencies
    pip install -U -r requirements.txt && \
# Add dev dependencies
    pip install -U -r requirements_dev.txt && \
# Make entrypoint executable
    chmod +x entrypoint.sh
