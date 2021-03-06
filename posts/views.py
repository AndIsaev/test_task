from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    View)
from .forms import PostForm
from .models import Post, User, Follow


class IndexView(ListView):
    """Main page."""
    model = Post
    template_name = "index.html"
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    """View one post."""
    model = Post
    context_object_name = "post"
    template_name = "includes/post.html"


class CreateNewPost(LoginRequiredMixin, CreateView):
    """Create new post."""
    model = Post
    form_class = PostForm
    template_name = "new_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.id})


class BlogViewList(LoginRequiredMixin, ListView):
    """Personal blog for author."""
    model = User
    template_name = "blog.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        author = User.objects.get(username=self.kwargs["username"])
        context["author"] = author
        posts = author.posts.all()
        context["posts"] = posts
        following = author.following.count()
        context["following"] = following
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Delete post, permission only for author."""
    model = Post
    template_name = "includes/post.html"
    success_url = reverse_lazy("index")


class FollowView(LoginRequiredMixin, View):
    """View for subscription."""
    def get(self, request, *args, **kwargs):
        author = get_object_or_404(
            User,
            username=self.kwargs["username"])
        if request.user != author:
            Follow.objects.get_or_create(
                user=request.user,
                author=author)

        return redirect("blog", username=self.kwargs["username"])


class UnFollowView(LoginRequiredMixin, View):
    """View for unsubscribe."""
    def get(self, request, *args, **kwargs):
        subscribe = Follow.objects.filter(
                user=request.user,
                author=get_object_or_404(
                    User,
                    username=self.kwargs["username"])
            )

        author = User.objects.get(username=self.kwargs["username"])
        user = User.objects.get(username=request.user)
        read_posts = user.read_post.filter(author=author)
        for noted_element in read_posts:
            user.read_post.remove(noted_element)
        subscribe.delete()
        return redirect("blog", username=self.kwargs["username"])


class FavoriteAuthorsView(LoginRequiredMixin, ListView):
    """View favorite authors."""
    model = Follow
    template_name = "favorite.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        authors = query.filter(user=self.request.user).values_list("author")
        posts = Post.objects.filter(author__in=authors)
        return posts


class ReadPostView(LoginRequiredMixin, View):
    """View for mark posts."""
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        if request.user not in post.read_post.all():
            post.read_post.add(request.user)

        else:
            post.read_post.remove(request.user)
        return redirect("post_detail", pk=self.kwargs["pk"])
