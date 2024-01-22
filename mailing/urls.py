from django.urls import path

from mailing.views import NewsletterListView

app_name = 'mailing'

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
]