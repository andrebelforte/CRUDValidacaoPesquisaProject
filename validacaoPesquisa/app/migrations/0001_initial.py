# Generated by Django 4.2.4 on 2023-08-12 03:27

import django.core.validators
from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('ano', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000)])),
                ('valor', models.FloatField()),
                ('data_cadastro', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
            ],
        ),
    ]