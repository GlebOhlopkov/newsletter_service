from django.db import models

from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='name')
    comment = models.TextField(null=True, blank=True, verbose_name='comment')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class Newsletter(models.Model):
    PERIOD_CHOICES = [
        ("PER_DAY", "every day"),
        ("PER_WEEK", "every week"),
        ("PER_MONTH", "every month"),
    ]
    STATUS_CHOICES = [
        ("CREATE", "create"),
        ("END", "end"),
        ("IN_WORK", "in work"),
    ]
    theme_massage = models.CharField(max_length=50, verbose_name='theme')
    text_massage = models.TextField(verbose_name='text')
    send_time_start = models.DateTimeField(verbose_name='newsletter send time start')
    send_time_finish = models.DateTimeField(verbose_name='newsletter send time finish')
    period = models.CharField(max_length=30, choices=PERIOD_CHOICES, verbose_name='period')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='CREATE', verbose_name='status')
    last_send_time = models.DateTimeField(null=True, blank=True, verbose_name='last try to send')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    clients = models.ManyToManyField(Client, verbose_name='clients')

    def __str__(self):
        return f'{self.theme_massage}: ({self.send_time_start}, {self.period}) - {self.user}'

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
        permissions = [
            (
                'moderator_view',
                'Moderator can view any newsletter'
            )
        ]


class LogNewsletter(models.Model):
    datetime_send = models.DateTimeField(blank=True, null=True, verbose_name='newsletter send time')
    status = models.CharField(max_length=30, blank=True, null=True, verbose_name='send status')
    server_answer = models.CharField(max_length=30, blank=True, null=True, verbose_name='server status')
    newsletter = models.IntegerField(verbose_name='newsletter id')

    def __str__(self):
        return f'{self.datetime_send}: {self.status}'

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
