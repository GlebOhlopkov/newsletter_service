from django.urls import path

from mailing.views import NewsletterListView, NewsletterCreateView, NewsletterDetailView, NewsletterUpdateView, \
    NewsletterDeleteView, ClientCreateView, ClientListView, LogNewsletterDetailView, LogNewsletterListView

app_name = 'mailing'

urlpatterns = [
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_create', ClientCreateView.as_view(), name='client_create'),
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_view'),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('lognewsletter/<int:pk>/', LogNewsletterDetailView.as_view(), name='lognewsletter_view'),
    path('lognewsletter/<int:pk>/', LogNewsletterListView.as_view(), name='lognewsletter_list')
]
