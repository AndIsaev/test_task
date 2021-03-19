from django.urls import path

from .views import IndexView, PostDetailView, BlogView, CreateNewPost, PostDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('new/', CreateNewPost.as_view(), name='new'),
    path("blog/<str:username>/", BlogView.as_view(), name="blog"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete_post/', PostDeleteView.as_view(), name='post_delete'),





]