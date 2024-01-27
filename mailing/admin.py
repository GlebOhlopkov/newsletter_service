from django.contrib import admin
from mailing.models import Newsletter, LogNewsletter, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'comment',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme_massage', 'text_massage', 'send_time_start',
                    'send_time_finish', 'period', 'status', 'user',)


@admin.register(LogNewsletter)
class LogNewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime_send', 'status', 'server_answer', 'newsletter',)
