# README

> 参考了[这个博客](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)


## 待合并项目

我的[网站](https://www.frankscarlet.pro/)

[现有App](https://github.com/FrankScarlet/Django_Apps)


## 改进

- 增加了国内源配置

## 待完成内容

- 静态主页plate应用
- 增加redis部分
- 增加blog部分

## Cheatsheet

### web+postgres

```shell
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec db psql --username=postgres --dbname=django_db
docker volume inspect django-docker_postgres_data
```

### dev and prod

```shell
docker-compose down -v
# Bring down the development containers (and the associated volumes with the -v flag)
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml logs -f # 查看日志
```

### 不理解

```shell
docker-compose up -d --build
docker-compose exec web python manage.py startapp upload
# 这一步为啥会在本地app文件夹里新建一个app啊
# 而且是root权限的...这不合适吧

# setting.py 临时注释掉用于生成新app
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
(env) python manage.py startapp upload
```