from django.urls import path
import imp
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
