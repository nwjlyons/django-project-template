from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from {{ project_name }}.views.pages import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view()),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Static files
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
