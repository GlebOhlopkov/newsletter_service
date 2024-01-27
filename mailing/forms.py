from django import forms
from django.forms import CheckboxInput, Select

from mailing.models import Newsletter, Client


class BootstrapFormStyleMixin:
    fields: dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_bootstrap_classes()

    def _add_bootstrap_classes(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class NewsletterForm(BootstrapFormStyleMixin, forms.ModelForm):
    send_time_start = forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])
    send_time_finish = forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])

    class Meta:
        model = Newsletter
        fields = ('theme_massage', 'text_massage', 'send_time_start',
                  'send_time_finish', 'period', 'status', 'clients',)
