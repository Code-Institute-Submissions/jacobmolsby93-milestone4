from . import views
from django.urls import path

app_name = "articles"

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('search/', views.search_view, name='search'),
    path('create/', views.ArticleCreate.as_view(), name='article_create'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
]