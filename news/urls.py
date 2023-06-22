from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("news/", PostListView.as_view(), name="news_list"),
    path("news/<int:pk>", PostDetailView.as_view(), name="news_detail"),
    path("news/create", PostCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/edit/", PostUpdateView.as_view(), name="news_update"),
    path("news/<int:pk>/delete/", PostDeleteView.as_view(), name="news_delete"),
    path("articles/", PostListView.as_view(), name="article_list"),
    path("articles/<int:pk>", PostDetailView.as_view(), name="article_detail"),
    path("articles/create", PostCreateView.as_view(), name="article_create"),
    path("articles/<int:pk>/edit/", PostUpdateView.as_view(), name="article_update"),
    path("articles/<int:pk>/delete/", PostDeleteView.as_view(), name="article_delete"),
    path(
        "news/search/", PostListView.as_view(template_name="search.html"), name="search"
    ),
]
