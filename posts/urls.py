from django.urls import path

from .views import (
    IndexView,
    PostDetailView,
    BlogViewList,
    CreateNewPost,
    PostDeleteView,
    FollowView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('new/', CreateNewPost.as_view(), name='new'),
    path("blog/<str:username>/", BlogViewList.as_view(), name="blog"),
    path('<str:username>/', FollowView.as_view(), name='follow'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete_post/', PostDeleteView.as_view(), name='post_delete'),

]