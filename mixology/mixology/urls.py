from django.conf.urls import patterns, include, url
from django.contrib import admin
from mixology import views
import drink
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixology.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^drink/', include('drink.urls', namespace='drink')),
    url(r'^$', drink.views.main, name='main'),
    url(r'^search/', drink.views.advanced_search, name='search')
)
