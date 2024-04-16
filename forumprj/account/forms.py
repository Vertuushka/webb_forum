# from django.contrib.auth.forms import UserCreationForm

# # Customize a UserCreationForm - remove unused texts
# class SignupUserForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password1'].help_text = None
#         self.fields['password2'].help_text = None
#     class Meta(UserCreationForm.Meta):
#         fields = ['username', 'password1', 'password2', 'email']
#         help_texts = {'username': None, 'email': None}

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Customize a UserCreationForm - use placeholders and hide labels
class SignupUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set placeholders and remove labels
        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].widget.attrs['placeholder'] = fieldname.capitalize()
            self.fields[fieldname].label = False
            self.fields[fieldname].help_text = None

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {
            'username': None,
            'email': None
        }

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set placeholders and remove labels
        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs['placeholder'] = fieldname.capitalize()
            self.fields[fieldname].label = False
            self.fields[fieldname].help_text = None

    class Meta():
        fields = ['username', 'password']
        help_tests = {
            'username': None,
            'password': None
        }