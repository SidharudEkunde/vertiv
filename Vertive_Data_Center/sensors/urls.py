from django.urls import path
from . import views

urlpatterns = [
    # URl for TemperatureHumidityAPI(get, post, delete, patch)
    path('sensor/temperature', views.TemperatureHumidityAPI.as_view()),

    # URL for DailyTemperatureHumidityAPI (get)
    path('sensor/dailydata', views.DailyTemperatureHumidityAPI.as_view()),

    # URL for WeeklyTemperatureHumidityAPI (get)
    path('sensor/weeklydata', views.WeeklyTemperatureHumidityAPI.as_view()),

    # URL for MonthlyTemperatureHumidityAPI (get)
    path('sensor/monthlydata', views.MonthlyTemperatureHumidityAPI.as_view()),

    # URL for IAQAPI(get, post, delete, patch)
    path('sensor/iaq', views.IAQAPI.as_view()),

    # URL for HealthAPI(get)
    path('sensor/health', views.HealthAPI.as_view()),

    path('system/daily', views.SystemRealtimeTrackingAPI.as_view()),

    path('system/weekly', views.WeeklyRealtimeTrackingAPI.as_view()),

    path('system/monthly', views.MonthlyRealtimeTrackingAPI.as_view()),

]
