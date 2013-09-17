from django.conf import settings
from django.conf.urls import patterns, include, url

from core.views import EventsContactFormView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', include('core.urls', namespace="core")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contato/$', EventsContactFormView.as_view(), name="contact_form"),
    url(r'^contato/sucesso/$',
        'core.views.contact_success',
        name="contact_form_sent"),
    url(r'^(?P<page>\w+)/$', 'core.views.pages', name='pages'),

)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns(
    '',
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, }),
    url(
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, }),
)
