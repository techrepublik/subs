from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_view, name='location_view'),
    path('load-provinces/', views.load_provinces, name='load_provinces'),
    path('load-municipalities/', views.load_municipalities, name='load_municipalities'),
    path('load-barangays/', views.load_barangays, name='load_barangays'),
]
