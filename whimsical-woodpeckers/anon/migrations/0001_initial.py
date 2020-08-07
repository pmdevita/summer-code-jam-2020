# Generated by Django 3.1 on 2020-08-07 05:42

from django.db import migrations, models
import django.utils.timezone
import namegenerator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnonUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(default=namegenerator.gen, max_length=40)),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(default='abcde', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
