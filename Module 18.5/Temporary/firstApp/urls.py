from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register_user , name="register_user"),
    path('login/', views.user_login, name="user_login"),
    path('Logout/', views.user_logout, name="user_logout"),
    path('profile/', views.profile , name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/edit/pass_change_with_password', views.change_pass_old, name="change_pass_old"),
    path('profile/edit/pass_change_without_password', views.change_pass, name="change_pass"),
]