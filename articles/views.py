from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth import get_user_model
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm, ArticleForm


class ArticleCreate(View):
    model = Article
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        article_form = ArticleForm(request.GET or None)
        context = {
            "article_form": article_form,
        }

        if article_form.is_valid():
            article_form = article_form.save(commit=False)
            article_form.user = request.user
            article_form.save()
        else:
            article_form = ArticleForm()

        return render(
            request,
            "create.html", 
            context=context,
        )
    
    def post(self, request, *args, **kwargs):
        article_form = ArticleForm(request.POST or None)
        context = {
            "article_form": article_form,
        }
        if article_form.is_valid():
            article_form = article_form.save(commit=False)
            article_form.user = request.user
            article_form.save()
            return redirect('home')
        else:
            article_form = ArticleForm()

        return render(
            request,
            "create.html", 
            context=context
        )


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('likes', '-published')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        return context


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        ) 

    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ArticleLike(View):

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)

        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))