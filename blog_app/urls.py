from django.urls import path
from blog_app.views import list_of_articles

app_name = 'blog_app'

urlpatterns = [
    path( '' , list_of_articles, name= 'list_of_articles' ),
]