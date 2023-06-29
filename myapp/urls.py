from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planets/', views.planets, name='planets'),
    path('moons/', views.moons, name='moons'), 
    path('SolarSistem', views.solarSistem, name='solarSistem')
]
