from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def shedule_email(email_Id):
    from jwtauth.models import EmailPush
    email_data=EmailPush.objects.get(id=email_Id)
    send_mail(
        subject=email_data.subject,
        message=email_data.message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email_data.reciever],
    )
    email_data.email_send=True
    email_data.save()

