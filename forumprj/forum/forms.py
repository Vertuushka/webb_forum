from django.contrib.auth.forms import UserChangeForm
      
# Customize a UserCreationForm - remove unused texts
class UpdateUserInfo(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']
        help_texts = {'username': None, 'email': None,}