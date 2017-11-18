from django.conf.urls import include, url
from django.contrib import admin

from whereami.views import whoami
from whereami.urls import urlpatterns as whereami_urlpatterns

from django.views.generic.base import RedirectView


urlpatterns = [
	url(r'^$', RedirectView.as_view(url='whoami.html', permanent=True)),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += whereami_urlpatterns
