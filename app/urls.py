from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.conf.urls import url

from .views import home, signup, Profile, edit_profile, upload, index

urlpatterns = [
    url(r'', home, name='home'),
    url(r'signup/', signup, name='signup'),
    url(r'upload/', upload, name='upload'),
    url(r'profile/<username>/', Profile, name='profile'),
    url(r'profile/<username>/settings', edit_profile, name='edit'),
    url(r'account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
