# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fish_name', models.CharField(verbose_name='Название', max_length=128, unique=True)),
                ('fish_text', models.TextField(verbose_name='Описание')),
                ('fish_image', models.ImageField(verbose_name='Изображение', upload_to='')),
                ('fish_date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'db_table': 'fish',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='fish',
            field=models.ForeignKey(to='fishlist.Fish'),
        ),
    ]
