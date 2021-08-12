from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),
    path('portfolio/', include('portfolio.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
