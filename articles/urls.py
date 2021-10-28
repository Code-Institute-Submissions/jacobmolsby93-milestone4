from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('create/', views.ArticleCreate.as_view(), name='article_create'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
]