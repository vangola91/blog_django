from django.urls import path
from blog_app.views import list_of_articles, article_details

app_name = 'blog_app'

urlpatterns = [
    path('', list_of_articles, name= 'list_of_articles'),
    path('<int:id>/', article_details, name='article_details'),
]