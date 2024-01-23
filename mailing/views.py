from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import NewsletterForm
from mailing.models import Newsletter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')

