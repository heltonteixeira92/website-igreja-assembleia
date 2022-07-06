from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError('Usuário ou senha inválidos.')
            if not user.email_verified:
                raise forms.ValidationError('Email não verificado, por favor veja sua caixa de e-mail')
        return super(LoginForm, self).clean()
