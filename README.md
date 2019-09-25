# Изучаем веб-разработку на Python/Djangо

[Django](https://djangoproject.com) — веб-фреймворк, написанный на языке 
Python, позволяющий быстро создавать проекты любой сложности: от простого 
сайта, до бэкендов сложных приложений.

На сентябрь 2019г актуальная версия Django==2.2.5. Для работы с данным 
фреймворком требуется [установить Python](https://python.org) не ниже 
версии 3.6.

1.1 Для начала работы создайте папку для проекта, например learn_django, в удобном 
для вас месте. Дальнейшие действия будут производиться в этой папке. 
```bash
mkdir learn_django
cd learn_django
```

## Работа с pip и virtualenv

2.1. Инициализация нового python окружения
```bash
python3 -m venv venv
```

2.2. Активировать акружение. Это необходимо делать каждый раз,
когда вы начинаете работать с проектом в командной строке.
```bash
source venv/bin/activate
```
Понять, что вы сейчас в окружении, можно по виду командной строки
```bash
(venv) $  
```

``(venv)`` в начале строки говорит о том, что вы сейчас находитесь
в виртуальном окружении проекта

2.3. Установка Django в окружение
```bash
pip install django
```

2.4. Записать установленные пакеты вместе с их версиями в файл
```bash
pip freeze > requirements.txt
```

**Опционально**:
* Показать установленные пакеты
```bash
pip freeze
```
* Выйти из виртуального окружения
```bash
deactivate
```
* Показать какие версии пакета django (или любого другого) доступны для установки
```bash
pip install django==
```

## Создание проекта Django

3.1. Создадим файловую структуру проекта. Точка в конце команды говорит о том,
что файловая структура будет создана в текущей папке. Мы вcе еще должны находиться
в папке learn_django, которую мы создале на этапе 1.1
```bash
django-admin startproject learn_django .
```

3.2. Запустить веб-сервер с проектом, пока с пустым
```bash
./manage.py runserver
```
После запуска этой команды можно зайти в любом браузере на http://localhost:8000
Если вы видете надпись "The install worked successfuly! Congratulations!", то
установка прошла успешно, можно приступать к следующим шагам.

3.3. Применить миграции. (*Миграция* — файл с описанием таблиц в базе данных)
```bash
./manage.py migrate
```

3.4. Созданим django-приложение. Приложение — это часть проекта,
выполняющая определенную роль. Например, личный кабинет в 
проекте интернет-магазина может быть приложением.
```bash
./manage.py startapp firstapp
```

3.5. Добавим приложение **firstapp** в список INSTALLED_APPS
установленных приложений проекта в файле настроек 
learn_django/settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',  # <---ЗДЕСЬ
]
``` 

и подключим к проекту папку *templates*, чтобы Django видел 
где будут находиться шаблоны
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # <---ЗДЕСЬ
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```
3.5. Внутри нашего проекта создадим папку templates, в которой 
создадим файл base.html c содержимым

templates/base.html
```djangotemplate
<html>
<head>
    <title>Learn Django Together</title>
</head>
<style>
    .main-wrapper {
        max-width: 1080px;
        margin: 0 auto;
    }
    .main-container {
        width: 100%;
        padding-top: 100px;
        text-align: center;
    }
</style>
<body>
<div class="main-wrapper">
    <div class="main-container">
        {% block content %}
        {% endblock %}
    </div>
</div>
</body>
</html>
``` 
3.6. Также в папке templates создадим еще один шаблон:

templates/firstapp.html
```djangotemplate
{% extends 'base.html' %}
{% block content %}
    <h1>Учим Django Вместе!</h1>
{% endblock %}
```
base.html и firstapp.html очень похожи на простые html-файлы. 
Единственное отличие — наличие тегов Django Template Language или 
DTL. Тег ``{% block content %}`` в шаблоне base.html дает 
возможность поместить в него содержимое, если данный шаблон 
будет использоваться для расширения другого. В нашем случае 
шаблон firstapp.html расширяет шаблон base.html. Делается 
это с помощью тега ``{% extends 'base.html' %}``, далее 
содержимое блока ``{% block content %}`` помещается в 
соответствующий блок base.html. В более сложных проектов может 
быть несколько вложенных шаблонов, расширяемых друг друга.
Для включения html-кода в шаблон используется тег 
``{% include 'template_name.html' %}``  

