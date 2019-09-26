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
