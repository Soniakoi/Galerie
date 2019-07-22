from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'galerie'),
    url(r'^pics(\d+)',views.pics,name='pics'),
    url(r'^search/',views.search_pics,name='search_pics'),
    url(r'^photos/',views.photos,name='photos'),
    url(r'^location/(\w+)',views.pics_location,name='location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)