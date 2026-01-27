from django.contrib import admin
from django.urls import path, include
from notes.views import status_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("status", status_view, name="status"),
    path("", include("notes.urls")),
]
