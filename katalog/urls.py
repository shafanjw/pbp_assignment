from katalog.views import show_catalogs
from django.urls import path

app_name = "katalog"

urlpatterns = [
    path("", show_catalogs, name="show_catalogs"),
]