from django.urls import path
from . import views
urlpatterns = [
        path('',views.book,name='book'),
        path('results',views.results,name='results'),
        path('login',views.login,name='login'),
        path('register',views.register,name='register'),
        path('logout',views.logout,name='logout'),
    
]