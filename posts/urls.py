from django.urls import path
from .views import (
    IndexView,
    PostDetailView,
    BlogViewList,
    CreateNewPost,
    PostDeleteView,
    FollowView,
    UnFollowView,
    FavoriteAuthors
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('new/', CreateNewPost.as_view(), name='new'),
    path("blog/<str:username>/follow", BlogViewList.as_view(), name="blog"),
    path('blog/<str:username>/unfollow', FollowView.as_view(), name='follow'),
    path('<str:username>/unfollow/', UnFollowView.as_view(), name='unfollow'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete_post/', PostDeleteView.as_view(), name='post_delete'),
    path('<str:username>', FavoriteAuthors.as_view(), name="favorite")

]