from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.display, name='display'),    
    url(r'^search/', views.search_category, name='search_category')
]     

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
