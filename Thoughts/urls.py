from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from Thoughts.views import index
from . import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Thoughts.views.index'), # root
    url(r'^login$', 'Thoughts.views.login_view'), # login
    url(r'^logout$', 'Thoughts.views.logout_view'), # logout
    url(r'^signup$', 'Thoughts.views.signup'), # signup
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)