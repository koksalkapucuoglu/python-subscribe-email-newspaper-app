from __future__ import absolute_import, unicode_literals

from datetime import date

from celery.utils.log import get_task_logger
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from core.celery import app
from newspaper import models

logger = get_task_logger(__name__)


@shared_task
def send_hardcoded_email_task():
    subject = 'Celery Task Worked!!'
    message = 'This is proof the task worked!'
    email_from = settings.EMAIL_HOST_USER
    recipent_list = ['hokera2282@iucake.com']

    return send_mail(
        subject, message, email_from, recipent_list, fail_silently=False
    )

@shared_task(bind=True)
def send_email_task(self, recipent_list, subject, message):
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipent_list = recipent_list

    return send_mail(
        subject, message, email_from, recipent_list, fail_silently=False
    )

def get_subscribed_email():
    return list(
        models.EmailSubscribe.objects.all().values_list('email', flat=True)
    )


@app.task()
def publish_daily_newspaper():
    daily_newspaper = models.Newspaper.objects.filter(publish_date=date.today())
    content = ''

    if daily_newspaper.exists():
        content = daily_newspaper[0].content
        subject = f'Newspaper - {date.today()}'
        email_from = settings.EMAIL_HOST_USER
        recipent_list = get_subscribed_email()

        return send_mail(
            subject, content, email_from, recipent_list, fail_silently=False
        )