from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from config import settings
from mailing.forms import NewsletterForm, ClientForm
from mailing.models import Newsletter, Client, LogNewsletter

from datetime import datetime


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:newsletter_list')


class ClientListView(ListView):
    model = Client


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')

    def form_valid(self, form):
        newsletter = form.save()
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
        return redirect('mailing:newsletter_list')


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class LogNewsletterDetailView(DetailView):
    model = LogNewsletter


class LogNewsletterListView(ListView):
    model = LogNewsletter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(newsletter_id=self.kwargs.get('pk'))
        return queryset
