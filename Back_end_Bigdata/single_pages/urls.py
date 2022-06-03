from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('data/', views.dataview),
    path('', views.landing),
]