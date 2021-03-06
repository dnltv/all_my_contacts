from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import (ChoiceField, DateInput, EmailInput, ImageField,
                          ModelForm, Textarea, TextInput)
from django.forms.formsets import formset_factory
from django.forms.models import BaseInlineFormSet, inlineformset_factory

from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # add  'reg_id' and 'code'
        fields = ('email', 'first_name',)
        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
        }


class EditDopeUserModelForm(ModelForm):

    class Meta:
        model = DopeUser
        exclude = ['user', 'first_name', 'slug']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
            }),
            'date_of_birth': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите дату рождения',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'photo': ImageField(),
            'status': ChoiceField(),
        }


class DopeUserForm(forms.ModelForm):

    class Meta:
        model = DopeUser
        exclude = ['user', 'slug']


class SocialMediaForm(ModelForm):

    class Meta:
        model = SocialMedia
        exclude = ['user']


# UserFormset = formset_factory(DopeUserForm)
