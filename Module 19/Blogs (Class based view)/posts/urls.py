
from django.urls import path
from . import views

urlpatterns = [
    # path('add_posts/', views.add_post, name='add_posts'),
    path('add_posts/', views.Add_post_ClassBasedView.as_view(), name='add_posts'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('edit/<int:id>/', views.Edit_post_ClassBasedView.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
    
    path('details/<int:id>/', views.postDetailView.as_view(), name='post_detail'),
]