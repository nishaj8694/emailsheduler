from django.db import models
from django.contrib.auth.models import User
from django .dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.utils.timezone import is_naive
import pytz
from jwtauth.task import shedule_email



class EmailPush(models.Model):
    reciever=models.EmailField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)
    Push_time=models.DateTimeField()
    email_send=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reciever}+_+{self.Push_time}"
         


@receiver(post_save, sender=EmailPush)
def shedule_email_create(sender,instance,created,**kwargs):
        
        if created:
            want_time=instance.Push_time
            indian_timezone = pytz.timezone('Asia/Kolkata')
            custom_datetime = datetime(want_time.year, want_time.month, want_time.day, want_time.hour, want_time.minute)  # Naive datetime

            if is_naive(custom_datetime):
                custom_datetime = indian_timezone.localize(custom_datetime)
                    
            shedule_email.apply_async(args=[instance.id], eta=custom_datetime)
























            #     push_time = instance.Push_time.astimezone(pytz.utc)
        #     print('mnt',push_time.minute)
        #     print('hour=',push_time.hour)
        #     print('day_of_month=',push_time.day)
        #     print('month',push_time.month)
        #     # print('day_of_week',push_time.week)
        #     crontab_schedule, created = CrontabSchedule.objects.get_or_create(
        #     minute=push_time.minute,
        #     hour=push_time.hour,
        #     day_of_month=push_time.day,
        #     month_of_year=push_time.month,
        # )

        # # Create a periodic task linked to this crontab
        #     PeriodicTask.objects.create(
        #         crontab=crontab_schedule,
        #         name=f"Send Email Task for {instance.id}",
        #         task='jwtauth.task.shedule_email',  # The task name as per your Celery task
        #         args=json.dumps([instance.id]),  # Arguments to the task, passed as a JSON array
        #         one_off=True  # Make sure this task only runs once
        #     )