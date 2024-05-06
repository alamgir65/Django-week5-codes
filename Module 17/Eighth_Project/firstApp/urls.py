

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup , name='signup'),
    path('login/', views.user_login , name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='user_logout'),
    path('passchange/', views.pass_change, name='passchange'),
    path('passchange2/', views.pass_change2, name='passchange2'),
]
