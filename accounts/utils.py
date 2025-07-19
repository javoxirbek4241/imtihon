import string, random
from django.core.mail import send_mail
from conf.settings import DEFAULT_FROM_EMAIL

def generate_code():
    letters = string.ascii_letters + string.digits
    return ''.join(letters[random.randint(0, len(letters) - 1)] for _ in range(6))
def send_to_mail(email, code):
    subject = 'Confirm code'
    message = f'Code {code}'

    send_mail(subject=subject,
    message=message,
    from_email=DEFAULT_FROM_EMAIL,
    recipient_list=[email, ])