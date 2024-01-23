from django import forms
from django.forms import CheckboxInput, Select

from mailing.models import Newsletter


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


class NewsletterForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
