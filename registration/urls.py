from django.urls import path, include
from . import views


urlpatterns = [
    # all the things you already have
    path("api/", include("oscarapi.urls")),
    path(
        'register/', views.UserRegistration.as_view(),
        name="user_registration"
    ),
    path(
        'users/', views.GetUser.as_view(), name="get_users"
    ),
]
