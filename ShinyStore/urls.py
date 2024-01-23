
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('', include('shiny.urls')),
    path('', include('users.urls')),
    path('user/', include('users.urls', namespace='user')),
    path('accounts', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
