from django.urls import path

from oscarapi.app import application as api

urlpatterns = (
    # all the things you already have
    path('oscarapi/', api.urls),
)