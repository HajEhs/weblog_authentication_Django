from django.views import generic
from django.shortcuts import reverse
from django.urls import reverse_lazy

from .models import Blog
from .forms import BlogForm
class PostListView(generic.ListView):
    template_name = "weblog/post_list.html"
    context_object_name = "post_pub"

    def get_queryset(self):
        return Blog.objects.filter(status="pub").order_by("-modified_datetime")

class PostDetailView(generic.DetailView):
    model = Blog
    template_name = "weblog/post_detail.html"
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    form_class = BlogForm
    template_name = "weblog/post_create.html"
    context_object_name = "form"

class PostUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "weblog/post_update.html"
    context_object_name = 'form'

class PostDeleteView(generic.DeleteView):
    model = Blog
    template_name = "weblog/post_delete.html"
    success_url = reverse_lazy("post_list")

    # def get_success_url(self):
    #     return reverse('post_list')
