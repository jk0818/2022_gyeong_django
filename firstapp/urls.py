from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post),
    path('req/ajax4/', views.req_ajax4),
    path('static/', views.static),
    path('var/', views.var),
    path('tag/', views.tag),
    path('filter/', views.filter),


]

