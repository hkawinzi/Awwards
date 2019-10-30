from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from . import views

from .views import home, signup, Profile, edit_profile, upload, index

urlpatterns = [
    url('', home, name='home'),
    url('signup/', signup, name='signup'),
    url('upload/', upload, name='upload'),
    url('profile/<username>/', Profile, name='profile'),
    url('profile/<username>/settings', edit_profile, name='edit'),
    url('account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
