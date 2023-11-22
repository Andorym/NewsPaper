from django.urls import reverse_lazy
from django.dispatch import Signal
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from NewsPaper.simpleapp.filters import PostFilter
from NewsPaper.simpleapp.forms import PostForm
from .models import Post
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post
    ordering = 'news'
    template_name = 'news.html'
    context_object_name = 'news'
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['time_now'] = datetime.utcnow()
       context['next_sale'] = None
       context['filterset'] = self.filterset
       return context

class Search(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name ='post_search'
    ordering = ['-dateCreation']
    filter_class = PostFilter
    paginate_by = 10

    def get_queryset(self):
      queryset = super().get_queryset()
      self.filter = self.filter_class(self.request.GET, queryset=queryset)
      return self.filter.qs.all()

addpost = Signal()

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

@method_decorator(login_required, name='dispath')
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name= 'post_create.html'
    form_class = PostForm
    
    def form_valid(self, form):
        post = form.save()
        id = post.id
        a = form.cleaned_data['postCategory']
        category_object_name = str(a[0])
        addpost.send(Post, instance=post, category=category_object_name)
        return super().form_valid(form)
    
 
class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

   

@method_decorator(login_required, name='dispath')
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

   