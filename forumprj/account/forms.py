from django import forms
from django.contrib.auth.models import User
      
class SignupUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password', 'email']
        help_texts = {'username': None}
        widgets = {'password': forms.PasswordInput()}
