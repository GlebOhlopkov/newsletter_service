from django.urls import path

from mailing.views import NewsletterListView, NewsletterCreateView, NewsletterDetailView, NewsletterUpdateView, \
    NewsletterDeleteView

app_name = 'mailing'

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_view'),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
]
