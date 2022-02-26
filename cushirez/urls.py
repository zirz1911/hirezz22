from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import members

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include(members.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)