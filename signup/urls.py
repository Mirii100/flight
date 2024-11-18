from django.urls import path
from . import views
urlpatterns = [
    path('',views.signUp,name='signin'),
    path('booking',views.booking,name='booking'),
     path('/reserve',views.reservation,name='reserve'),

]