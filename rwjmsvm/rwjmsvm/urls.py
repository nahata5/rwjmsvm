from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rwjmsvm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^virtualmicroscope/', include('nyuvm.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', include(admin.site.urls)),
    url(r'^virtualmicroscope/admin/', include(admin.site.urls)),
)
