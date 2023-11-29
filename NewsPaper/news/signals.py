from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers
from .models import Category
from django.db.models.signals import post_delete

@receiver(post_save, sender=Category)
def notify_managers_subscribers(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.user_name}{instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'Category changed for {instance.user_name} {instance.date.strftime("%d %m %Y")}'
    mail_managers(subject=subject, message=instance.message)
    post_save.connect(notify_managers_subscribers,sender=Category)


@receiver(post_delete, sender=Category)
def notify_managers_subscribers_canceled(sender, instance, **kwargs):
   subject = f'{instance.user_name} has cancelled subscription!'
   mail_managers(subject=subject, message=f'Subscription cancelled for{instance.date.strftime("$d $m $Y")}')
   print(subject)