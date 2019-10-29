from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

from .views import home, signup, Profile, edit_profile, upload, index

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('upload/', upload, name='upload'),
    path('profile/<username>/', Profile, name='profile'),
    path('profile/<username>/settings', edit_profile, name='edit'),
    path('account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
