from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, DopeUser
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name')


class EditDopeUserModelForm(ModelForm):

    class Meta:
        model = DopeUser
        exclude = ['user', 'first_name', 'slug']

