# README

## 0512 

### 生成密钥

```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 拷贝Volume

> 从Schedule_bot的Volume拷贝到本地，再从本地拷到Container里

```bash
docker cp [src] [des]
docker cp mediafiles/ djangodocker_bot_1:/home/app/web/botfiles/
# 我写错了，拷到web里了，结果权限就乱了....现在那个拷贝的就没法删除掉了（因为已经切换到appuser用户了）
```


## 待完成内容

- [ ] 增加redis部分

## 参考

- [bootstrap博客模板](https://djangocentral.com/building-a-blog-application-with-django/)

- 我的[网站](https://www.frankscarlet.pro/)

- [原有App](https://github.com/FrankScarlet/Django_Apps)

-  Docker方式部署参考了[这个博客](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)


## Cheatsheet

> 启动与停止，可用VS Code（包括查看容器内内容，容器内执行命令）

### pre

```bash
# 一会儿再补
docker-compose -f docker-compose.pre.yml up -d --build
# 因为变动了数据库
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations
# 由于引入了mdeditor，需要重新收集静态资源
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```


### dev

```shell
docker-compose up -d --build
docker-compose down
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

### prod

```shell
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
docker-compose -f docker-compose.prod.yml exec db psql --username=postgres
# Bring down the development containers (and the associated volumes with the -v flag)
docker-compose -f docker-compose.prod.yml down
# -v 会把volume去掉的，，，
```



## FAQ

如何新建应用

```shell

docker-compose exec web python manage.py startapp upload
# 这一步为啥会在本地app文件夹里新建一个app啊
# 而且是root权限的...这不合适吧，VS Code都没法编辑了

# 推荐使用虚拟环境来新建，当然不用应该也行
(env) python manage.py startapp upload
# setting.py 临时注释掉用于生成新app
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
```

