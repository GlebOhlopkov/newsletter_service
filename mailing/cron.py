from mailing.models import Newsletter
from django.conf import settings
from django.core.mail import send_mail


def start_newsletter_in_work():
    newsletter_set = Newsletter.objects.all()
    for newsletter in newsletter_set:
        if newsletter.status == 'CREATE':
            newsletter.status.set('IN_WORK')


def send_newsletter_per_day():
    newsletter_set = Newsletter.objects.all()
    for newsletter in newsletter_set:
        if newsletter.status == 'IN_WORK' and newsletter.period == 'PER_DAY':
            clients = newsletter.clients.all()
            for client in clients:
                send_mail(
                    subject=f'{newsletter.theme_massage}',
                    message=f'{newsletter.text_massage}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )


def send_newsletter_per_week():
    newsletter_set = Newsletter.objects.all()
    for newsletter in newsletter_set:
        if newsletter.status == 'IN_WORK' and newsletter.period == 'PER_WEEK':
            clients = newsletter.clients.all()
            for client in clients:
                send_mail(
                    subject=f'{newsletter.theme_massage}',
                    message=f'{newsletter.text_massage}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )


def send_newsletter_per_month():
    newsletter_set = Newsletter.objects.all()
    for newsletter in newsletter_set:
        if newsletter.status == 'IN_WORK' and newsletter.period == 'PER_MONTH':
            clients = newsletter.clients.all()
            for client in clients:
                send_mail(
                    subject=f'{newsletter.theme_massage}',
                    message=f'{newsletter.text_massage}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
