from django.conf.urls import patterns, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^siteadmindetail/$',       views.siteadmin_detail,                                  name='siteadmindetail'),
    url(r'^advertdisplay/$',         views.advert_display,                                    name='advertdisplay'),
    url(r'^advertinsert/$',          views.advert_insert,                                     name='advertinsert'),
    #url(r'^advertupdate/$',          views.advert_update,                                     name='advertupdate'),
)