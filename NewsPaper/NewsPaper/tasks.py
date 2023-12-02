import datetime
from celery import shared_task
import time
from django.core.mail import send_mail
from news.models import Category, Post

@shared_task
def mailing():
    list_recipients =[]
    date_from = datetime.datetime.now() - datetime.timedelta(days=7)
    for category in Category.objects.all():
        list_recipients.clear()
        for user in category.subscribers_user.all():
            list_recipients.append(user.email)
        posts = Post.objects.filter(category=category, date_time_in__gte=date_from)
