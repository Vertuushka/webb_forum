from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'email', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'formInput',
                'placeholder': field_name.capitalize()
            })

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'email']

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs.update({
                'class': 'formInput',
                'placeholder': field_name.capitalize()
            })

    class Meta:
        fields = ['username', 'password']