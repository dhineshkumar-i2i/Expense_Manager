# Generated by Django 4.0.3 on 2022-05-02 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)])),
                ('phone_number', models.BigIntegerField(validators=[django.core.validators.RegexValidator(code='invalid_number', message='Phone number must be 10 digits', regex='^[789]\\d{9}$')])),
                ('salary', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('email', models.EmailField(max_length=254)),
                ('created_by', models.IntegerField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
