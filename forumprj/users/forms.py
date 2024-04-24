from django.contrib.auth.forms import UserChangeForm

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