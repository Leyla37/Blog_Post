from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm
from django.core.paginator import Paginator
from django.db.models import Q  
from django.http import HttpResponse
from rest_framework import generics
from .serializers import BlogPostSerializer



class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer




class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    # paginate_by = 5


    def get(self, request, *args, **kwargs):
        blog_list = BlogPost.objects.all()
        paginator = Paginator(blog_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print("Current page number:", page_number)  
        return render(request, 'blog/blog_list.html', {"page_obj": page_obj})
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return queryset


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class BlogCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

