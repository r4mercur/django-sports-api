from django.urls import path

from . import views

app_name = "competitions"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index")
]
