from datetime import datetime
import pytz

from mailing.models import Newsletter, LogNewsletter
from django.conf import settings
from django.core.mail import send_mail


def start_newsletter_in_work():
    newsletter_list = Newsletter.objects.all()
    for newsletter in newsletter_list:
        if newsletter.status == 'CREATE':
            newsletter.status.set('IN_WORK')


def send_newsletter():
    newsletter_list = Newsletter.objects.all()
    for newsletter in newsletter_list:
        if newsletter.status == 'IN_WORK' and newsletter.period == 'PER_DAY':
            local_tz = pytz.timezone('Europe/Minsk')
            time = datetime.now()
            local_time = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_start = newsletter.send_time_start.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_finish = newsletter.send_time_finish.replace(tzinfo=pytz.utc).astimezone(local_tz)
            if newsletter.last_send_time:
                local_last_send_time = newsletter.last_send_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
                delta = local_time - local_last_send_time
                try:
                    if local_time_start <= local_time < local_time_finish and delta.days >= 1:
                        clients = newsletter.clients.all()
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
            else:
                try:
                    if local_time_start <= local_time < local_time_finish:
                        clients = newsletter.clients.all()
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

        elif newsletter.status == 'IN_WORK' and newsletter.period == 'PER_WEEK':
            local_tz = pytz.timezone('Europe/Minsk')
            time = datetime.now()
            local_time = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_start = newsletter.send_time_start.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_finish = newsletter.send_time_finish.replace(tzinfo=pytz.utc).astimezone(local_tz)
            if newsletter.last_send_time:
                local_last_send_time = newsletter.last_send_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
                delta = local_time - local_last_send_time
                try:
                    if local_time_start <= local_time < local_time_finish and delta.days >= 7:
                        clients = newsletter.clients.all()
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
            else:
                try:
                    if local_time_start <= local_time < local_time_finish:
                        clients = newsletter.clients.all()
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
        elif newsletter.status == 'IN_WORK' and newsletter.period == 'PER_MONTH':
            local_tz = pytz.timezone('Europe/Minsk')
            time = datetime.now()
            local_time = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_start = newsletter.send_time_start.replace(tzinfo=pytz.utc).astimezone(local_tz)
            local_time_finish = newsletter.send_time_finish.replace(tzinfo=pytz.utc).astimezone(local_tz)
            if newsletter.last_send_time:
                local_last_send_time = newsletter.last_send_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
                delta = local_time - local_last_send_time
                try:
                    if local_time_start <= local_time < local_time_finish and delta.days >= 30:
                        clients = newsletter.clients.all()
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
            else:
                try:
                    if local_time_start <= local_time < local_time_finish:
                        clients = newsletter.clients.all()
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
