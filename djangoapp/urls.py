from django.conf.urls.defaults import patterns, include, url
from djangoapp.views import hello,home,current_datetime,pikka_name,host
from djangoapp.books import views
from djangoapp.contact import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     ('^hello/$', hello),	
     ('^$', home),
     ('^time/$', current_datetime),	 		
     ('^pikka/$', pikka_name),
     ('^host/$', host),
#     (r'^search-form/$', views.search_form),	
#     (r'^search/$', views.search),
     (r'^contact/$', views.contact),	
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^djangoapp/', include('djangoapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
