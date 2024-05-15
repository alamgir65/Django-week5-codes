from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.set_session, name='home'),
    # path('get/', views.get_cookies, name='get_cookies'),
    path('get/', views.get_session, name='get_cookies'),
    # path('del/', views.delete_cookies, name='delete_cookies'),
    path('del/', views.delete_session, name='delete_cookies'),
]