from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('',views.home, name='article-home'),
    path('article/<str:title>/<int:article_id>/',views.fullArticle, name='fullArticle'),
    path('add-article/',views.addArticle, name='addArticle'),
    path('edit-article/<str:title>/<int:article_id>/',views.editArticle, name='editArticle'),
    path('view-profile/<str:username>/',views.viewProfile, name='viewProfile'),
    path('article/search/',views.search, name='search')
]