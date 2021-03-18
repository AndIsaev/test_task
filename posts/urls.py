from django.urls import path

from .views import IndexView, PostDetailView, BlogView, CreateNewPost

urlpatterns = [
    path('new/', CreateNewPost.as_view(), name = 'new'),
    path('<slug:pk>/', PostDetailView.as_view(), name='post_detail'),

    path("", IndexView.as_view(), name="index"),
    path("<str:username>/", BlogView.as_view(), name="blog"),


]