from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from Thoughts.views import index
from Thoughts.views import login_view
from Thoughts.views import logout_view
from Thoughts.views import signup
from mysite.views import search_form
from mysite.views import search
from mysite.views import register
#from mysite.views import new_post
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
               #url(r'^$', index), # root
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^account/social/accounts/$", TemplateView.as_view(template_name="account/social.html"), name="account_social_accounts"),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
    url(r"^frontpage/", TemplateView.as_view(template_name="frontpage.html"), name="front"),
    url(r"^post_form/$", search_form),
    url(r"^posts/$", search),
    url(r"^register/$", register),
    url(r"^home/", TemplateView.as_view(template_name="frontpage.html"), name="front"),
    url(r'^$', 'Thoughts.views.index'), # root
    url(r'^login$', 'Thoughts.views.login_view'), # login
    url(r'^logout$', 'Thoughts.views.logout_view'), # logout
    url(r'^signup$', 'Thoughts.views.signup'), # signup
               #url(r'^post$', new_post, name='new_post')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
