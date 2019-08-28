from django.urls import path
from . import views

urlpatterns = [
    path('culture/', views.culture_display, name='culture_display'),
    path('trend/', views.region_trend, name='region_trend'),
]