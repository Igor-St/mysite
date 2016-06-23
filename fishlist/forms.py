# -*- coding: utf8 -*-
from django import forms
from django.contrib.auth.models import User
from fishlist.models import Fish, Comment, UserProfile


class FishForm(forms.ModelForm):
    fish_name = forms.CharField(max_length=128, label="Название")
    fish_text = forms.TextInput()
    fish_image = forms.ImageField(label="Изображение")

    class Meta:
        model = Fish
        exclude = ('fish_date',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        exclude = ('comment_date',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)



