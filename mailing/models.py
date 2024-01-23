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
    send_time = models.TimeField(verbose_name='newsletter time')
    period = models.CharField(choices=PERIOD_CHOICES, verbose_name='period')
    status = models.CharField(choices=STATUS_CHOICES, default='CREATE', verbose_name='status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    clients = models.ManyToManyField(Client, verbose_name='clients')

    def __str__(self):
        return f'{self.theme_massage}: ({self.send_time}, {self.period}) - {self.user}'

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'


class LogNewsletter(models.Model):
    datetime_send = models.DateTimeField(blank=True, null=True, verbose_name='last datetime send')
    status = models.CharField(blank=True, null=True, verbose_name='send status')
    server_answer = models.CharField(blank=True, null=True, verbose_name='server status')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.DO_NOTHING, verbose_name='newsletter')

    def __str__(self):
        return f'{self.datetime_send}: {self.status}'

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
