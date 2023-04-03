from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from blog_app.models import Article


def list_of_articles(request):
    articles = Article.publishedArticles.all()
    # print(articles)

    return render(request, 'blog/list.html', {'articles': articles})

def article_details(request, id):
    try:
        article = get_object_or_404(Article, id=id, status=Article.Status.PUBLISHED)
    except Article.DoesNotExist:
        raise Http404("No article found.")
    return render(request, 'blog/detail.html', {'article': article})