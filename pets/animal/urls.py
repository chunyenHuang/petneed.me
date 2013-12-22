# app specific urls
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from animal.views import LostAnimalCreate

urlpatterns = patterns('',
    url(r'^home', 'animal.views.home'),
    url(r'^page/', 'animal.views.page'),
    url(r'^profile/(?P<animal_id>\d+)/$', 'animal.views.profile', name='profile'),
    url(r'^login', 'animal.views.login_view'),
    url(r'^logout', 'animal.views.logout_view'),
    url(r'^API/0.1/animals/$', 'animal.views.get_animals'),
    url(r'^API/0.1/animal/(?P<accept_num>\d+)/$', 'animal.views.get_specific_animal'),
    url(r'^facebook_login', 'animal.views.facebook_login'),
    url(r'^register$', 'animal.views.register'),
    url(r'^facebook_register$', 'animal.views.facebook_register'),
    url(r'^thanks', 'animal.views.thanks'),
    url(r'^upload', 'animal.views.upload'),
    url(r'^user_profile', 'animal.views.user_profile'),
    url(r'lost/add/$', LostAnimalCreate.as_view(), name='LostAnimal_add'),
    url(r'^find$', 'animal.views.find_animal'),
    url(r'^find/(?P<page_num>\d+)$', 'animal.views.find_animal_page'),
    url(r'^find/upload', 'animal.views.find_animal_upload'),
    #url(r'^get_img', 'animal.views.get_img'),
)
