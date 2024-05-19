from profile_messages.models import Private_Message
from django.contrib.auth.models import User
import re
from django.db.models import Q

def profile_processor(request):
    chat_data = {}
    if request.path.startswith('/profile/'):
        match = re.search(r'(\d+)', request.path)
        if match:
            user_id = int(match.group(1))
            try:
                account = User.objects.get(id=user_id)
                private_messages = Private_Message.objects.filter(
                    Q(sender=request.user, receiver=account) | Q(sender=account, receiver=request.user)
                ).order_by('-id')
                chat_data["private_messages"] = private_messages
                chat_data["dialog"] = private_messages[0].dialog
            except:
                chat_data["private_messages"] = False
    return chat_data
                