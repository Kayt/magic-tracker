from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.vary import vary_on_headers
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('tbxcodingtask.tracker.urls')),
    path('django-admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
