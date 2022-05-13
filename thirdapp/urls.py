from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/', views.jeju_olle),
    path('jeju_olle/ajax/', views.jeju_olle_ajax),
    path('owner/', views.owner),
]