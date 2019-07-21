from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'galerie'),
    url(r'^search/', views.search_images, name='search_images'),
]