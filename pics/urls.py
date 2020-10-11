from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url('^$',views.index, name = 'index'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^search/', views.search_category, name='search_category')
]     
    