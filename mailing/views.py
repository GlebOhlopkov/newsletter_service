from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from config import settings
from mailing.forms import NewsletterForm, ClientForm
from mailing.models import Newsletter, Client, LogNewsletter

from datetime import datetime


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:newsletter_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')

    def form_valid(self, form):
        newsletter = form.save(commit=False)
        newsletter.user = self.request.user
        newsletter.save()
        time = datetime.now().time()
        if time >= newsletter.send_time:
            clients = newsletter.clients.all()
            for client in clients:
                send_mail(
                    subject=f'{newsletter.theme_massage}',
                    message=f'{newsletter.text_massage}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
        return super().form_valid(form)


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    permission_required = 'moderator_view'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404("Sorry, you don't owner of this newsletter")
        return self.object


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404("Sorry, you don't owner of this product")
        return self.object


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class LogNewsletterDetailView(LoginRequiredMixin, DetailView):
    model = LogNewsletter


class LogNewsletterListView(LoginRequiredMixin, ListView):
    model = LogNewsletter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(newsletter_id=self.kwargs.get('pk'))
        return queryset
