# Generated by Django 4.1.7 on 2023-04-23 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mynotes_alter_user_signup_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(blank=True, default=datetime.datetime(2023, 4, 23, 12, 46, 15, 577021))),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 23, 12, 46, 15, 577021)),
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 23, 12, 46, 15, 577021)),
        ),
    ]