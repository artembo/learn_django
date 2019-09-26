# Веб-разработка Python/Djangо

Содержание занятия:
* [Начало работы](#1--)
* [pip и virtualenv](#2-pip--virtualenv)
* [Создание проекта Django](#3---django)
* [Модели](#4-)

## 1. Начало работы

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

## 2. pip и virtualenv

Виртуальное окружение — это изолированная среда с отдельным 
интерпретатором python и установленными пакетами. Как правило,
одно виртуальное окружение создается для одного проекта.

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

## 3. Создание проекта Django

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
```bash
(venv) learn_django user$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 26, 2019 - 07:31:03
Django version 2.2.5, using settings 'learn_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

После запуска этой команды можно зайти в любом браузере на адрес
локального сервера http://127.0.0.1:8000.
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
        width: 100%;
    }
    .main-container {
        margin: 0 auto;
        max-width: 400px;
        padding-top: 100px;
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
будет использоваться для расширения другого. 

В нашем случае шаблон firstapp.html расширяет шаблон base.html. 
Делается это с помощью тега ``{% extends 'base.html' %}``, далее 
содержимое блока ``{% block content %}`` помещается в 
соответствующий блок base.html. 

В более сложных проектах может быть несколько вложенных 
шаблонов, расширяемых последовательно. В шаблонах DTL 
может быть любое количество расширяемых блоков.

Для включения html-кода в шаблон используется тег 
``{% include 'template_name.html' %}``, eго мы будем использовать в 
слудующих уроках.

3.7. firstapp/views.py

В Django view (Вью, редко — представление) — это модуль, который получает 
http запрос (request) и выдает ответ (response). Запрос на сервер
происходит каждый раз, когда вы набираете адрес сайта и нажимаете
enter, когда кликаете мышкой по ссылке и тд. Запрос включает в 
себя инфонмацию о пользователе, версию браузера, адрес откуда 
исходит запрос и многое другое, что можно использовать во view
при формировании ответа.

В простом случае, как описанов в коде ниже, происходит 
отправка шаблона, который мы сделали ранее на любой запрос.

```python
from django.shortcuts import render

def index(request):
    return render(request, 'firstapp.html')

```

3.8. firstapp/urls.py
Осталось соединить сам путь нашей первой странички с view.
За это отвечает файл urls.py, а точнее переменная *urlpatterns*
в нем. Она хранит в себе список путей (path), которые "соединяют"
путь на нашем сервере с view.

```python
from django.urls import path

from firstapp.views import index

urlpatterns = [
    path('', index)
]
```

Если мы посмотрим в папку learn_django, то там уже будет
файл urls.py, созданный автоматически командой (3.1). 
Это входная точка для всех *путей* проекта, на что
указывает специальная переменная в файле настроек 
learn_django/settings.py ``ROOT_URLCONF = 'learn_django.urls'``

Модифицируем файл `learn_django/urls.py` таким образом,
чтобы он включал в себя созданный нами `firstapp/urls.py`

3.8.1 learn_django/urls.py
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls'))
]

```

Теперь круг замкнулся. Пользователь в браузере пишет путь, 
который соответствует **path** в `urls.py`, **path** направляет
запрос пользователя на view ``def index(request):``,
эта view рендерит и отправляет обратно html, взятый из 
двух DTL файлов: `base.html` и `firstapp.html`

3.8. Запустим сервер разработки Django еще раз и проверим
```bash
./manage.py runserver
```

## 4. Модели
4.1. Спроектируем и создадим первые модели.
Пока все слишком просто и не хватает динамики в проекте.

Для хранения инфирмации в бд Django использует собственный
механизм абстракций, называемы моделями. При проектировании 
приложения (сайта, программы и тд) в современной практике 
используют ООП, согласно которому *модель сопоставляется с
объектом в реальной жизни рассматриваемой проедметной области*.

Рассмотрим простую базу данных с людьми и их контактами:

Какими свойствами обладает человек? Пусть у нашего человека
в БД будет три параметра:

**Человек**
* Имя
* День рождения
* Пол

Какими свойствами обладает контакт человека?

**Контакт**
* Название (Телеграм, VK, Почта, LinkedIn и тд)
* Путь
* Человек (Любой контакт пренадлежит определенному человеку)

Перенесем описание объектов БД (человек и его контакт) в 
модели Django:

firstapp/models.py
```python
from django.db import models


class Person(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    birthday = models.DateField('День рождения')
    gender = models.BooleanField('Пол', default=True)

    def __str__(self):
        return '{} {}'.format(self.fio, self.gender)


class Contact(models.Model):
    person = models.ForeignKey('firstapp.Person', models.CASCADE, related_name='contacts')
    service = models.CharField('Сервис', max_length=100)
    link = models.CharField('Ссылка', max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.service, self.link)
```

Метод модели `def __str__(self):` служит для удобного 
отображения экземпляра модели, например, в админ. панели Django

Зарегистрируем модели в админке:

firstapp/admin.py
```python
from django.contrib import admin

from firstapp.models import Person, Contact

admin.site.register(Person)
admin.site.register(Contact)
```

Обратим внимание на листинг 3.8.1. В нем содержится путь 
``path('admin/', admin.site.urls)`` а значит, можно зайти
в браузере по адресу http://127.0.0.1:8000/admin/

Вы попадете на страницу авторизации пользователей Django 

Создать первого и самого влиятельного пользователя в проекте
можно командой:

```bash
./manage.py createsuperuser
```

После успешного создания пользователя можно авторизоваться
и добавить неслолько человек и их контактов через 
административную панель Django.

4.2 Модификация view и шаблона для демонстрации людей и их 
контактов на сайте.

Передадим в шаблон всех людей через контекст.

Контекст — это python словарь, содержащий данные, используемые
в шаблоне.

Изучите изменения в листингах ниже, внесите соответствующие
изменения, после чего проследите как изменилась страница
со списком людей и их контактов http://127.0.0.1:8000

firstapp/views.py
```python
from django.shortcuts import render

from firstapp.models import Person


def index(request):
    people = Person.objects.all()
    context = {
        'people': people
    }
    return render(request, 'firstapp.html', context)
```

templates/firstapp 
```djangotemplate
{% extends 'base.html' %}

{% block content %}
    <h1>Учим Django Вместе!</h1>

        {% for person in people %}
            <h2>{{ person.fio }}</h2>
            <h3>Пол: {% if person.gender %}мужской{% else %}женский{% endif %}</h3>
            <h3>Дата рождения: {{ person.birthday }}</h3>
            <ul>
                {% for contact in person.contacts.all %}
                    <li><strong>{{ contact.service }}: </strong><span>{{ contact.link }}</span></li>
                {% empty %}
                    <li>{{ person.fio }} контактов немеет</li>
                {% endfor %}
            </ul><br>

            {% if not forloop.last %}
                <hr>
            {% endif %}

        {% endfor %}
{% endblock %}
```

