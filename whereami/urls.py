from django.conf.urls import url

from . import views

urlpatterns = [
	url('^whoami.html$', view=views.whoami, name='whoami-landing'),
    url('^travels/', views.travel_list, name='travel-list'),
    url('^art/', views.art_list, name='art-list'),
    url('^paintings/', views.painting_list, name='painting-list'),
    url('^collages/', views.collage_list, name='collage-list'),
    url('^linos/', views.lino_list, name='lino-list'),
    url('^installations/', views.installation_list, name='installation-list'),
    url('^travel/(?P<pk>\d+)/$', view=views.travel_details, name='travel-details'),

]
