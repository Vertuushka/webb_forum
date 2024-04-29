from typing import Any
from django.contrib.auth.forms import UserChangeForm
from django import forms
from . models import Preference

# Customize a UserCreationForm - remove unused texts
class UpdateUserInfo(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
    class Meta(UserChangeForm.Meta):
        fields = ['last_name', 'email']
        labels = {
            'last_name': 'forum title'
            }
        help_texts = {'username': None, 'email': None,}

class UserPreferences(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['color_theme', 'account_visibility', 'private_messages']