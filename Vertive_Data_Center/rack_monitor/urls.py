from rest_framework.urls import path
from . import views

urlpatterns = [
    path('rack', views.RackAPI.as_view())
]
