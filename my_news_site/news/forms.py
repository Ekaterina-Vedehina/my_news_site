from django import forms
from .models import Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок новости:',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, label='Текст новости:',
                              widget=forms.Textarea(attrs={"class": "form-control",
                                                           "rows": 5}))
    is_published = forms.BooleanField(initial=True, label='Опубликовать:')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория:',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off",
                                                             "autofocus": "None"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off",
                                                             "autofocus": "None"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))