Веб-разработка Python/Djangо. Workshop 2.
=========================================

.. contents:: Содержание занятия
    :depth: 2

1. Git. Основы. Запускаем готовый проект Django
-----------------------------------------------

Git — это система контроля версий проекта.

Склонируем проект с установленным шаблоном Bootstrap4

.. code:: bash

   git clone -b lesson-02 https://github.com/artembo/learn_django.git learn_django_02

-  зайдите в папку ``learn_django_02`` — это репозиторий с проектом, вся
   работа по его
   `созданию <https://github.com/artembo/learn_django/blob/master/book/lessons/lesson-02.rst>`__
   уже выполнена, осталось сделать несколько простых шагов, чтобы
   запустить его.

-  создайте виртуальное окружение, активируйте его и установите пакеты,
   необходимые для запуска приложения из requirements.txt

.. code:: bash

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

-  примените миграции

.. code:: bash

   ./manage.py migrate

-  создайте суперпользователя для доступа к админ. панели Django

.. code:: bash

   ./manage.py createsuperuser

-  запустите сервер разработки django

.. code:: bash

   ./manage.py runserver

-  пополните список контактов через админ. панель, либо пополните БД с
   помощью фикстуры

.. code:: bash

   ./manage.py loaddata fixture.json

-  откройте в браузере страницу http://127.0.0.1:8000 и посмотрите
   результат работы приложения


2 Расширяем возможности приложения
----------------------------------

На данный момент возможности нашего проекта сильно ограничены. Мы можем
добавить контакты только через админ. панель Django. Также мы можем видеть
только весь список контактов на.

Сделаем отдельную страницу, на которой будет отображаться контакты только
одного конкретного человека.

Модели изменять не будем. Остается добавить 3 компонента приложения:

- template
- view
- url

Шаблон страницы контакта

templates/person.html

.. code:: html

    {% extends 'base.html' %}

    {% block content %}

        {% include 'contact_card.html' %}

    {% endblock %}

Добавим представление, отвечающее за получение данных человека и рендеринг
шаблона с его контактами

firstapp/views.py

.. code:: python

    def person_view(request, pk):
        person = Person.objects.get(pk=pk)
        context = {
            'person': person
        }
        return render(request, 'person.html', context)

А также добавим путь, по которому можно будет найти данную страницу

firstapp/urls.py

.. code:: python

    urlpatterns = [
        path('', index),
        path('person/<pk>/', person_view, name='person'),
    ]

Сделаем возможность перехода к персональной странице человека через
ссылку в списке.

Модифицируем файл templates/contact_card.html

.. code:: html

    <div class="card-title">
        <a href="{% url 'person' person.pk %}">{{ person.fio }}</a>
    </div>

Теперь на страницу персональную страницу можно зайти кликнув на имя
человека в списке

Добавим форму добавления контакта человека

Что для этого нужно?

- (forms.py) сама форма, которую мы добавим на страницу данных человека
- (views.py) представление, которое будет получать форму, проверять ее на валидность,
  и перенаправлять на страницу с сообщением об успешном добавлении контакта.
- (urls.py) путь к представлению, которое принимает форму, и путь к результирующей странице.

firstapp/forms.py

.. code:: python

    from django import forms
    from firstapp.models import Contact

    class ContactForm(forms.ModelForm):

        class Meta:
            model = Contact
            fields = ('service', 'link')

templates/person.html

.. code:: html

    {% extends 'base.html' %}

    {% block content %}

        {% include 'contact_card.html' %}

        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Добавить">
        </form>

    {% endblock %}

tamplates/contact_successfully_added.html

.. code:: html

    {% extends 'base.html' %}

    {% block content %}

        <h2>Контакт успешно добавлен</h2>

    {% endblock %}

firstapp/views.py

.. code:: python

    def person_view(request, pk):
        person = Person.objects.get(pk=pk)

        if request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.person = person
                contact.save()
                return render(request, 'contact_successfully_added.html')

        form = ContactForm()
        context = {
            'person': person,
            'form': form
        }
        return render(request, 'person.html', context)

3. Оптимизация приложения и запросов к БД
-----------------------------------------

3.1 Class-based views
~~~~~~~~~~~~~~~~~~~~~

firstapp/views.py

.. code::

    class IndexView(ListView):
        model = Person
        template_name = 'firstapp.html'
        context_object_name = 'people'

    class PersonContactCreateView(DetailView, CreateView):
        model = Person
        context_object_name = 'person'
        template_name = 'person.html'
        form_class = ContactForm
        success_url = reverse_lazy('contact_created')

        def get_initial(self):
            return {'person': self.kwargs.get('pk')}

    class ContactCreatedView(TemplateView):
        template_name = 'contact_successfully_added.html'

firstapp/urls.py

.. code:: python

    from django.urls import path

    from firstapp.views import index, person_view, ContactCreatedView, PersonContactCreateView, IndexView

    urlpatterns = [
        path('', IndexView.as_view(), name='index'),
        # path('person/<pk>/', person_view, name='person'),
        path('person/<pk>/', PersonContactCreateView.as_view(), name='person'),
        path('person/contact/created/', ContactCreatedView.as_view(), name='contact_created'),
    ]


3.2 django-debug-toolbar
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   pip install django-debug-toolbar

learn_django/settings.py

.. code:: python

    INSTALLED_APPS = [
        'registration',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'firstapp',
        'debug_toolbar',
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

Оптимизируем модель и шаблон:

.. code:: python

    class Person(models.Model):
        fio = models.CharField('ФИО', max_length=100)
        birthday = models.DateField('День рождения')
        gender = models.BooleanField('Пол', default=True)

        def get_contacts(self):  # <- новый метод модели
            return self.contacts.all()

        def __str__(self):
            gender = '(М)' if self.gender else '(Ж)'
            return '{} {}'.format(self.fio, gender)

.. code:: html

    <div class="col-md-4">
      <div class="card mb-4 shadow-sm">
        <div class="card-body">
          <div class="card-title">
              <a href="{% url 'person' person.pk %}">{{ person.fio }}</a>
          </div>
          <p class="card-text">Пол: {% if person.gender %}мужской{% else %}женский{% endif %}</p>
          <p class="card-text">Дата рождения: {{ person.birthday }}</p>
          <ul>
            {% for contact in person.get_contacts %}  # <- вызываем метод модели вместо обращения к бд
                <li><strong>{{ contact.service }}: </strong><span>{{ contact.link }}</span></li>
            {% empty %}
                <li>{{ person.fio }} контактов не имеет</li>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>

firstapp/views.py

.. code:: python

    class IndexView(ListView):
        queryset = Person.objects.prefetch_related('contacts')  # <- оптимизированный запрос
        template_name = 'firstapp.html'
        context_object_name = 'people'
