from django.urls import path
from . import views

urlpatterns = [
    path('culture/australia', views.au_display, name='au_display'),
    path('culture/china', views.cn_display, name='cn_display'),
    path('culture/new_zealand', views.nz_display, name='nz_display'),
    path('culture/uk', views.uk_display, name='uk_display'),
    path('culture/india', views.india_display, name='india_display'),
    path('culture/vietnam', views.vn_display, name='vn_display'),
    path('events', views.event_display, name='event_display'),
    path('events/search/', views.search, name='search'),
    path('map/', views.map_display, name='map_display'),
    path('community_garden/report', views.garden_report, name='garden_report'),
    path('community_garden/find', views.garden_find, name='garden_find'),
]