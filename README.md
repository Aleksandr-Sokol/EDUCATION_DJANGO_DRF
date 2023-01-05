# EDUCATION_DJANGO_DRF
## Шаблон проектов для django DRF

### Установка Django
pip install -r template_requirements.txt

### Создание нового проекта
django-admin startproject <имя проекта>

### Добавление приложения
python manage.py startapp <имя приложения>

### запустить миграцию базы данных
python manage.py migrate
### Для отбражения таблиц в admin нужно добавить их с декоратором 
@admin.register

### последующие миграции 
python manage.py  makemigrations <имя приложения>
python manage.py migrate

### создать суперпользователя
python.exe manage.py createsuperuser
http://127.0.0.1:8000/admin/login/

### Запуск проекта
python manage.py runserver 127.0.0.1:8000 

### Страница администратора
http://127.0.0.1:8000/admin/

### Установка swagger (django-rest-swagger)

https://django-rest-swagger.readthedocs.io/en/latest/

Ошибка: django.template.exceptions.TemplateSyntaxError: 'staticfiles' is not a registered tag library. Must be one of:...

Решение: Добавить 'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
В TEMPLATES (settings.py)

Другой swagger:
https://drf-yasg.readthedocs.io/en/stable/readme.html#quickstart