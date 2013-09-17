# coding: utf-8
from django import forms

from contact_form.forms import ContactForm


class EventsContactForm(ContactForm):
    name = forms.CharField(max_length=100,
                           label=u'Nome')
    email = forms.EmailField(max_length=200,
                             label=u'E-mail')
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': '15'}),
                           label=u'Mensagem')
    company = forms.CharField(max_length=100,
                              label=u'Empresa')
    telephone = forms.CharField(max_length=100,
                                label=u'Telefone')
