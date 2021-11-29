from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('',views.home, name='article-home'),
    path('article/<str:user>/<int:article_id>/',views.fullArticle, name='fullArticle'),
    path('add-article/',views.addArticle, name='addArticle'),
    path('edit-article/<str:user>/<int:article_id>/',views.editArticle, name='editArticle'),
]