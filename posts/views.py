from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView)
from .forms import PostForm, FollowForm
from .models import Post, User, Follow


class IndexView(ListView):
    """Main page."""
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """View one post."""
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'


class CreateNewPost(LoginRequiredMixin, CreateView):
    """Create new post."""
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})


class BlogViewList(ListView):
    """Personal blog for author"""
    model = User
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        author = User.objects.get(username=self.kwargs['username'])
        context['author'] = author
        posts = author.posts.all()
        context['posts'] = posts
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Delete post, permission only for author"""
    model = Post
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('index')


class FollowView(LoginRequiredMixin, CreateView):
    """View for subscription"""
    # model = Follow
    template_name = 'author.html'
    form_class = FollowForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = User.objects.get(username=self.request.user)
    #     author = User.objects.get(username=self.kwargs['username'])
    #     print(author, '-------------------------------------')
    #
    #     context['user'] = user
    #     context['author'] = author
    #     if user != author:
    #         Follow.objects.get_or_create(user=user, author=author)
    #     return context

    # def get_success_url(self):
    #     return redirect('index')

