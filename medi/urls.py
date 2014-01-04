from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'medi.views.home'),
    url(r'^home$', 'medi.views.home'),
    url(r'^about$', 'medi.views.about'),
    url(r'^login$', 'medi.views.login_view'),
    url(r'^register$', 'medi.views.sign_up'),


    #url(r'^upload/$', 'video_converter.views.upload'),
    #url(r'^s3direct/', include('s3direct.urls')),
    
    #api urls
    #url(r'^api/convert/$', 'video_converter.views.convert'),
    #url(r'^api/progress/$', 'video_converter.views.progress'),
    #url(r'^api/get_url/$', 'video_converter.views.get_url'),
)
