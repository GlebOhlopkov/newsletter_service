from django.db import models

from users.models import User


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
    time = models.TimeField(verbose_name='newsletter time')
    period = models.CharField(choices=PERIOD_CHOICES, verbose_name='period')
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return f'{self.time}: {self.period}, {self.status} ({self.user}'

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'


class Massage(models.Model):
    theme = models.CharField(max_length=50, verbose_name='theme')
    text = models.TextField(verbose_name='text')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='newsletter')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'massage'
        verbose_name_plural = 'massages'


class LogNewsletter(models.Model):
    datetime_send = models.DateTimeField(verbose_name='last datetime send')
    status = models.CharField(verbose_name='send status')
    server_answer = models.CharField(null=True, verbose_name='server status')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.DO_NOTHING, verbose_name='newsletter')

    def __str__(self):
        return f'{self.datetime_send}: {self.status}'

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
