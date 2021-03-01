from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT

api_urlpatterns = [
    path('', include('core.users.urls')),
    path('', include('core.posts.urls')),
]

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='api/v1/', view=include(api_urlpatterns)),
]

if DEBUG:
    from debug_toolbar import urls
    from django.conf.urls.static import static

    urlpatterns += (
        path(route='__debug__/', view=include(urls)),
        # path(route='silk/', view=include('silk.urls')),
    )
    urlpatterns += tuple(
        static(MEDIA_URL, document_root=MEDIA_ROOT)
    )
