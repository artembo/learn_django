# Занятие №1 Разработка первого django-приложения

Как запустить приложение

- склонируйте данный репозиторий
```bash
git clone -b lesson-01 https://github.com/artembo/learn_django.git
```

- зайдите в папку ``learn_django`` — это репозиторий с проектом, вся работа по его 
[созданию](https://github.com/artembo/learn_django/blob/master/book/lessons/lesson-01.rst) 
уже выполнена, осталось сделать несколько простых шагов, чтобы запустить его. 

- создайте виртуальное окружение, активируйте его и установите пакеты,
необходимы для запуска приложения из requirements.txt
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- примените миграции
```bash
./manage.py migrate
```

- создайте суперпользователя для доступа к админ. панели Django
```bash
./manage.py createsuperuser
```

- запустите сервер разработки django
```bash
./manage.py runserver
```

- пополните список контактов через админ. панель, либо пополните БД
с помощью фикстуры
```bash
./manage.py loaddata fixture.json
```

- откройте в браузере страницу http://127.0.0.1:8000 и посмотрите результат
работы приложения
