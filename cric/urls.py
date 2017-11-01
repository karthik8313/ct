from django.conf.urls import url,include
from django.contrib import admin
from . import views
from .models import india,Australia,South_Africa,England
from cric.views import indiaDetailView,australiaDetailView,south_africaDetailView,englandDetailView
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^india', views.india_v),
    url(r'^australia', views.australia_v),
    url(r'^south_africa', views.south_africa_v),
    url(r'^england', views.england_v),
    url(r'^detail-india/(?P<pk>[-\w]+)/$', indiaDetailView.as_view(), name='india-detail'),
    url(r'^detail-australia/(?P<pk>[-\w]+)/$', australiaDetailView.as_view(), name='australia-detail'),
    url(r'^detail-south_africa/(?P<pk>[-\w]+)/$', south_africaDetailView.as_view(), name='south_africa-detail'),
    url(r'^detail-england/(?P<pk>[-\w]+)/$', englandDetailView.as_view(), name='england-detail'),
    url(r'^register', views.newuser),
]
