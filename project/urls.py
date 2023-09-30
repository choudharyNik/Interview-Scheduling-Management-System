from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("requirements/", include("requirements.urls")),
    path("candidates/", include("candidates.urls")),
    path("interviews/", include("interviews.urls")),
]
