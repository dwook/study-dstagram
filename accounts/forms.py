from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

    def clean_password2(self):  # clean_필드명 형태의 메서드. 각 필드의 clean 메서드가 호출된 후에 호출되는 메서드.
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']

