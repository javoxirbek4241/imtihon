from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='parol', widget=forms.PasswordInput)
    password2= forms.CharField(label='parol', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 is None or password2 is None or password1!=password2:
            raise forms.ValidationError('parollarni bir xil ekanligini tekshiring')
        return password2
    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=120, label='username')
    password = forms.CharField(label='parol', widget=forms.PasswordInput)

class ChangePassForm(forms.Form):
    old_pass = forms.CharField(label='eski parol', widget=forms.PasswordInput)
    new_pass = forms.CharField(label='new parol', widget=forms.PasswordInput)
    confirm_pass = forms.CharField(label='parolni tasdiqlang', widget=forms.PasswordInput)
    code = forms.CharField(label='emailga yuborilgan kod', max_length=6)

    def clean(self):
        cleaned_data = super().clean()
        new_pass = cleaned_data.get('new_pass')
        confirm_pass = cleaned_data.get('confirm_pass')
        if new_pass and confirm_pass and new_pass != confirm_pass:
            raise forms.ValidationError('Parollar mos emas')
        return cleaned_data


class ResetPassForm(forms.Form):
    password = forms.CharField(label='Yangi parol', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput)
    code = forms.CharField(label='Tasdiqlash kodi', max_length=6)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Parollar mos emas')
        return cleaned_data















