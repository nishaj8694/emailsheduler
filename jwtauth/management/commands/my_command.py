from django.core.management.base import BaseCommand
from jwtauth.models import EmailPush
from jwtauth.task import shedule_email
from datetime import datetime,timezone
import pytz
from django.utils.timezone import is_naive

class Command(BaseCommand):
    help = 'Custom command to perform startup database operations'

    def handle(self, *args, **kwargs):
        email_data = EmailPush.objects.filter(email_send=False)
        for email in email_data:
            indian_timezone = pytz.timezone('Asia/Kolkata')
            custom_datetime = datetime(email.Push_time.year, email.Push_time.month, email.Push_time.day, 
                                     email.Push_time.hour, email.Push_time.minute) 

            if is_naive(custom_datetime):
                custom_datetime = indian_timezone.localize(custom_datetime) 

            now = datetime.now(pytz.timezone('Asia/Kolkata'))
            if custom_datetime>now:
                shedule_email.apply_async((email.id,),eta=custom_datetime)

        self.stdout.write(self.style.SUCCESS('Successfully performed operations.'))




