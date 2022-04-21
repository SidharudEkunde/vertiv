from rest_framework.urls import path
from . import views

urlpatterns = [
    # URL for alert(get)
    path('alert', views.AlertAPI.as_view()),
    path('alert/tracking', views.AlertTrackingAPI.as_view())
]
