from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        "message": "Welcome to the assignment project. Please import the API collection to your Postman and test the APIs."
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("restaurant.urls")),
    path("", include("user.urls")),
    path("", hello),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)