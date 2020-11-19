FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# change tsinghua mirror ?
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]