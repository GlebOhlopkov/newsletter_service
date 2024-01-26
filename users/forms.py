from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from mailing.forms import BootstrapFormStyleMixin
from users.models import User


class UserRegisterForm(BootstrapFormStyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(BootstrapFormStyleMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()