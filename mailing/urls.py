from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.views import NewsletterListView, NewsletterCreateView, NewsletterDetailView, NewsletterUpdateView, \
    NewsletterDeleteView, ClientCreateView, ClientListView, LogNewsletterDetailView, LogNewsletterListView, HomeView, \
    NewsletterModeratorUpdateView

app_name = 'mailing'

urlpatterns = [
    path('', cache_page(60)(HomeView.as_view()), name='home'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_create', ClientCreateView.as_view(), name='client_create'),
    path('newsletter_list', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/', cache_page(60)(NewsletterDetailView.as_view()), name='newsletter_view'),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter__moderator_update/<int:pk>/', NewsletterModeratorUpdateView.as_view(),
         name='newsletter_moderator_update'),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('lognewsletter/<int:pk>/', LogNewsletterDetailView.as_view(), name='lognewsletter_view'),
    path('lognewsletter/<int:pk>/', LogNewsletterListView.as_view(), name='lognewsletter_list')
]
