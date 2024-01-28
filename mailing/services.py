from datetime import datetime
import pytz
from django.core.mail import send_mail
from config import settings

from mailing.models import LogNewsletter


def send_newsletter_now(newsletter):
    local_tz = pytz.timezone('Europe/Minsk')
    time = datetime.now()
    local_time = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_time_start = newsletter.send_time_start.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_time_finish = newsletter.send_time_finish.replace(tzinfo=pytz.utc).astimezone(local_tz)
    if local_time_start <= local_time < local_time_finish:
        clients = newsletter.clients
        try:
            for client in clients:
                send_mail(
                    subject=f'{newsletter.theme_massage}',
                    message=f'{newsletter.text_massage}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
            newsletter.last_send_time = datetime.now()
            log = LogNewsletter.objects.create(datetime_send=datetime.now(), status='SEND',
                                               server_answer='DELIVER', newsletter=newsletter.id)
            log.save()
        except Exception:
            log = LogNewsletter.objects.create(datetime_send=datetime.now(), status='NOT SEND',
                                               server_answer='ERROR', newsletter=newsletter.id)
            log.save()
