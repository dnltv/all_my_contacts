from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, DopeUser
from django.forms import ModelForm, EmailInput, TextInput, DateInput, Textarea, ImageField, ChoiceField


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

