from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Secret

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(email=email, username=username).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        elif CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        return email




class SecretForm(forms.ModelForm):
    class Meta:
        model = Secret
        fields = ['text']
