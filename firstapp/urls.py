from django.urls import path
from . import views
app_name = 'firstapp'

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('insert/', views.insert),
    path('show/', views.show, name = 'show'),
    path('req/get/', views.req_get, name = 'req_get'),
    path('req/post/', views.req_post ),
    path('req/ajax4/', views.req_ajax4, name = 'req_post'),
    path('static/', views.static),
    path('var/', views.var),
    path('tag/', views.tag),
    path('filter/', views.filter),
    path('template/', views.template),
    path('form/model/', views.form_model),


]

