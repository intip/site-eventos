# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

# Third-party app imports
from contact_form.views import ContactFormView

# Imports from your apps
from .forms import EventsContactForm


def homepage(request):
    """
    Doc string
    """

    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


def pages(request, page):
    """
    """
    return render_to_response(
        page + ".html",
        context_instance=RequestContext(request)
    )


class EventsContactFormView(ContactFormView):
    form_class = EventsContactForm


def contact_success(request):
    """
    """
    return render_to_response(
        "contact_form/contact_form_sent.html",
        context_instance=RequestContext(request)
    )
