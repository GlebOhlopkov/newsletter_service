from datetime import datetime
import pytz

from django.core.mail import send_mail

from config import settings
from mailing.models import LogNewsletter


def send_newsletter_now(newsletter, time):
    utc = pytz.UTC
    time_start = utc.localize(newsletter.send_time_start)
    time_finish = utc.localize(newsletter.send_time_finish)
    if time_start <= time < time_finish:
        clients = newsletter.clients.all()
        try:
            for client in clients:
                print('send')
                # send_mail(
                #     subject=f'{newsletter.theme_massage}',
                #     message=f'{newsletter.text_massage}',
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=[client.email]
                # )
            newsletter.last_send_time = datetime.now()
            log = LogNewsletter.objects.create()
            log.datetime_send = datetime.now()
            log.status = 'SEND'
            log.server_answer = 'DELIVER'
            log.newsletter = newsletter.id
        except Exception:
            log = LogNewsletter.objects.create()
            log.datetime_send = datetime.now()
            log.status = 'NOT SEND'
            log.server_answer = 'ERROR'
            log.newsletter = newsletter.id