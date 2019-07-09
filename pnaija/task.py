from django.core.mail import send_mail
from .models import UserProfile


def send_email(user_id, subj):
  """
  Task to send an e-mail notification when an order is
  successfully created.
  """
  user = User.objects.get(id=user_id)
  subject = f'PNaija: {subj}'
  message = f'Dear {user.first_name}, \n\n Thank you for reaching us, we will get back to you.'
  mail_sent = send_mail(subject, message, 'uniqueomokenny@gmail.com', [user.email])

  return mail_sent