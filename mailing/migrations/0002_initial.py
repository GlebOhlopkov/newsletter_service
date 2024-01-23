# Generated by Django 4.2.9 on 2024-01-23 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='lognewsletter',
            name='newsletter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mailing.newsletter', verbose_name='newsletter'),
        ),
    ]
