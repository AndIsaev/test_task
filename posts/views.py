from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from .models import Post, User


class IndexView(ListView):
    """Main page."""
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class PostDetailView(DetailView):
    """View one post."""
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'


class BlogView(ListView):
    """Personal blog for author"""
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        username = User.objects.get(username=self.request.user)
        context['username'] = username
        print()
        print(username)


        return context


class CreateNewPost(CreateView):
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




