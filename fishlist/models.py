# -*- coding: utf8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Fish(models.Model):
    class Meta():
        db_table = 'fish'
    fish_name = models.CharField(verbose_name="Название", max_length=128, unique=True)
    fish_text = models.TextField(verbose_name="Описание")
    fish_image = models.ImageField(verbose_name="Изображение")
    fish_date = models.DateTimeField(verbose_name="Дата",auto_now_add=True)

    def __str__(self):
        return self.fish_name

class Comment(models.Model):
    class Meta():
        db_table = 'comments'
    fish = models.ForeignKey(Fish)
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username