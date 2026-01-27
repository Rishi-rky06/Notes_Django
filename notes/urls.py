from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.note_list, name="list"),
    path("new/", views.note_create, name="create"),
    path("<int:pk>/edit/", views.note_edit, name="edit"),
    path("<int:pk>/delete/", views.note_delete, name="delete"),
    path("login/", auth_views.LoginView.as_view(template_name="notes/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="notes:login"), name="logout"),
]
