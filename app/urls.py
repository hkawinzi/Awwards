from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^upload/$', views.upload, name='upload'),
    url(r'^profile/<username>/', views.Profile, name='profile'),
    url(r'^profile/<username>/settings', views.edit_profile, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
