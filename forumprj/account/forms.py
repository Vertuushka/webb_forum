from django.contrib.auth.forms import UserCreationForm
      
# Customize a UserCreationForm - remove unused texts
class SignupUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {'username': None, 'email': None}