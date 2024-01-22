from django.contrib import admin

from mailing.models import Newsletter, Massage, LogNewsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'period', 'status', 'user', )


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'text', 'newsletter', )


@admin.register(LogNewsletter)
class LogNewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime_send', 'status', 'server_answer','newsletter', )
