from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app1.models import Post, User


class RegisterForm(ModelForm):

   class Meta:
     model = User
     fields = '__all__'

class LoginForm(ModelForm):
    model = User



class CreatePost(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                    to_field_name = 'first_name',
                                    empty_label="")

    class Meta:
        model = Post
        fields = '__all__'

   







