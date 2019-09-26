# Generated by Django 2.2.5 on 2019-09-26 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('gender', models.BooleanField(default=True, verbose_name='Пол')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100, verbose_name='Сервис')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='firstapp.Person')),
            ],
        ),
    ]
