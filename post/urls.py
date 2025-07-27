from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('post_list/', views.post_list, name="post_list"),
    path('create_post/', views.create_post, name="create_post"),
    path('post_edit/', views.post_edit, name="post_edit"),
    path('delete_post/<int:pk>/', views.post_delete, name="post_delete"),
    path('<int:post_pk>/thumbnail/<int:image_pk>/', views.thumbnail_view, name='thumbnail'),
]
