from django.conf.urls import patterns
from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples for custom menu
    path("", include(admin.site.urls)),
)
