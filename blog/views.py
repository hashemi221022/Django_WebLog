from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import generic

from .models import Post
from .forms import PostForm

# from django.http import HttpResponse
#! ya fancinal base view mesle in(1)
# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

#! ya class base view mesle in(1)
class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
       return Post.objects.filter(status='pub').order_by('-datetime_modified')

# ya fancinal base view mesle in(2)

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # # except Post.DoesNotExist:
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print('NAN')
#     return render(request, 'blog/post_detail.html', {'post': post})

#! ya class base view mesle in(2)

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def create_post_view(request):
#     # print('this is test')
#     # print(request.method) #! show get request and post request
#     # print(request.POST) #! show title and text in a form that you create
#     # print(request.POST.get('title')) #! show only one (title)
#     # print(request.POST.get('text')) #! show only one (text
#     if request.method == 'POST': #! show get oe post request in if (shart)
#     #     print(f"title of post : {request.POST.get('title')}")
#     #     print(f"text of post : {request.POST.get('text')}")
#     # else:
#     #     print('Get request')
#         user = User.objects.all()[0]
#         post_title = request.POST.get('title')
#         post_text = request.POST.get('text')
#         Post.objects.create(title=post_title, text=post_text, author=user, status='pub') #!create client new post in database
#     else:
#         print('Get request')
#     return render(request, 'blog/post_create.html')

# def create_post_view(request):
#
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = PostForm()
#             return redirect('posts_list')
#
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post' : post})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')

