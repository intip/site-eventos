# coding: utf-8
from django import forms

from contact_form.forms import ContactForm

"""
  Campo de select para 'Assunto'
"""
subjects = (
    (u'0', u'Quero testar o sistema'),
    (u'1', u'Quero comprar'),
    (u'3', u'Dúvida'),
    (u'4', u'Outros'),
  )

"""
  Como de select para 'Como nos encontrou?'
"""
founds = (
    (u'0', u'Sites de buscas (Google, Bing, etc.)'),
    (u'1', u'Indicação'),
    (u'3', u'E-mail'),
    (u'4', u'Outros'),
  )

class EventsContactForm(ContactForm):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput({ "placeholder": "Digite seu nome..."}),
                           label=u'Nome')
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput({ "placeholder": "Digite seu E-mail..."}),
                             label=u'E-mail')
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}),
                           label=u'Mensagem',
                           required=False)
    company = forms.CharField(max_length=100,
                              label=u'Empresa',
                              required=False)
    telephone = forms.CharField(max_length=100,
                                widget=forms.TextInput({ "placeholder": "Digite seu telefone..."}),
                                label=u'Telefone')
    found = forms.ChoiceField(label=u'Como nos encontrou?',
                              choices=founds,
                              required=False)
    subject = forms.ChoiceField(label=u'Assunto',
                                choices=subjects,
                                required=False)