from django.conf.urls import patterns, include, url
from robokassa import urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^robokassa/', include('robokassa.urls')),
    url(r'^home/febo/(\d+)/([-+]?[0-9]*\.?[0-9]+)', 'myrobo.views.pay_with_robokassa'),
)
