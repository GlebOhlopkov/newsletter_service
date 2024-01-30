from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Blog
from mailing.forms import NewsletterForm, ClientForm, NewsletterModeratorForm
from mailing.models import Newsletter, Client, LogNewsletter

from mailing.services import send_newsletter_now


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
        send_newsletter_now(newsletter)
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


class NewsletterModeratorUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterModeratorForm
    success_url = reverse_lazy('mailing:newsletter_list')
    template_name = 'mailing/newsletter_moderator_form.html'


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


class HomeView(View):
    model1 = Newsletter
    model2 = Blog
    model3 = Client
    template_name = 'mailing/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            'newsletter_list' : self.model1.objects.all().count(),
            'newsletter_in_work': self.model1.objects.filter(status='IN_WORK').count(),
            'blog_list': self.model2.objects.all().order_by('-id')[:3],
            'client_list': self.model3.objects.all().count(),
        }
        return render(request, template_name=self.template_name, context=self.context)