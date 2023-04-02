from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Article


def list_of_articles(request):
    articles = Article.publishedArticles.all()
    # print(articles)

    return render(request, 'blog/list.html', {'articles': articles})