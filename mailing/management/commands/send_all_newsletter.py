from django.core.management import BaseCommand

from mailing.cron import send_newsletter


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_newsletter()
