from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from config import celery_app
from members.tokens import account_activation_token

User = get_user_model()

@celery_app.task
def send_mail():
    user = User.objects.last()

    message = render_to_string('account_activate_email.html', {
        'user': user,
        'domain': 'localhost:8000',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
        'token': account_activation_token.make_token(user)
    })

    mail_subject = 'test'
    to_email = user.username
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
