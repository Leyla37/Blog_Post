from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('api/posts/', views.BlogPostListCreateAPIView.as_view(), name='api_post_list_create'),
    path('api/posts/<int:pk>/', views.BlogPostDetailAPIView.as_view(), name='api_post_detail'),
]

