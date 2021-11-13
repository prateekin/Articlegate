from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.index ,name='index'),
    path('signin/', views.signIn ,name='signIn'),
    path('signup/', views.signUp ,name='signUp'),
]
