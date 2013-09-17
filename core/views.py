# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

# Third-party app imports

# Imports from your apps


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
