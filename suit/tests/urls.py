from django.urls import path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]
