from django.urls import path
from . import views
app_name = 'secondapp'   #namespace

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name = 'show'),
    path('army_shop/', views.army_shop, name = 'army_shop'),
    path('army_shop/<int:year>/<int:month>/',
        views.army_shop2),
     path('course/', views.course),
     path('course/save/', views.course_save),
]