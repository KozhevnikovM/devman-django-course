from django.contrib import admin
from django.urls import path, include
from where_to_go import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index),
    path('places/<int:place_id>', views.place_detail_view),
    path('tinymce/', include('tinymce.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
