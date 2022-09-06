from django import forms
from .models import User, UserProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

class RegistBaseForm(forms.ModelForm):
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # htmlのクラス属性を付加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = ['username', 'NUmail (xxx@g.nihon-u.ac.jp)', 'password']
        for i, field in enumerate(self.fields.values()):
            field.widget.attrs['class'] = 'input login-form__item'
            field.widget.attrs['placeholder'] = labels[i]

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()

        # User属性のデータ作成と連動してUserPfofile属性のデータ(デフォルト値)も追加
        UserProfile.objects.create(user=user, grade=6, department='秘密')

        return user

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = ['NUmail (xxx@g.nihon-u.ac.jp)', 'password']
        for i, field in enumerate(self.fields.values()):
            field.widget.attrs['class'] = 'input login-form__item'
            field.widget.attrs['placeholder'] = labels[i]

# class UserUpdateForm(forms.ModelForm):
#     grade = forms.CharField(label='')
#     department = forms.EmailField(label='')
#     image = forms.ImageField(label='')

#     class Meta:
#         model = UserProfile
#         fields = ['grade', 'department', 'image']