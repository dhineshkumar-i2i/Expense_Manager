# Generated by Django 4.0.3 on 2022-05-02 12:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], default='Expense', max_length=10)),
                ('created_by', models.IntegerField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_shared', models.BooleanField(default=False)),
                ('total_amount', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledger', to='category.category')),
                ('user', models.ManyToManyField(related_name='ledger', to='user.userdetails')),
            ],
        ),
    ]
