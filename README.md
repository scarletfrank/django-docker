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

### 开发环境下的相关命令

```shell
docker-compose up -d --build
docker-compose down -v
# Bring down the development containers (and the associated volumes with the -v flag)
# 可选命令
# entrypoint.sh里其实应该有migrate了
docker-compose exec web python manage.py migrate --noinput 
# 在？看看数据库。其实通过docker desktop里的cli访问更方便一点
docker-compose exec db psql --username=postgres --dbname=django_db_dev 
# 这个应该是跟nginx配合的，因为这个命令是把静态文件收集到一个固定的地方方便管理
# 顺带一提，搜索的关键词就是static
# 跟STATIC_URL没有关联，后者是绑定静态文件的访问路径/staticfiles/admin.css
docker-compose exec web python manage.py collectstatic --no-input --clear
# 看看volume
docker volume inspect django-docker_postgres_data
```

### 生产环境

带了static和media

```shell
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
# Bring down the development containers (and the associated volumes with the -v flag)
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml logs -f # 查看日志
```


### FAQ

```shell
docker-compose up -d --build
docker-compose exec web python manage.py startapp upload
# 这一步为啥会在本地app文件夹里新建一个app啊
# 而且是root权限的...这不合适吧，VS Code都没法编辑了

# setting.py 临时注释掉用于生成新app
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
(env) python manage.py startapp upload
```
