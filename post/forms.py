from django import forms
from django.contrib.auth.models import User
from . import models

class Form_createPost(forms.ModelForm):

    class Meta:
        model = models.post
        fields = ['title', 'content']


class Form_createComment(forms.ModelForm):

     class Meta:
        model = models.comment
        fields = ['content', 'origin_post']

