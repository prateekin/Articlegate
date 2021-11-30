from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context = {
        # 'posts': Post.objects.all()
        # stores top 50 liked objects
        'posts' : Post.objects.order_by('-likes')[:50]
    }
    return render(request , 'article/home1.html', context)

def fullArticle(request,title,article_id):
    # print(article_id)
    # user = User.objects.get(id=request.user.pk)
    post = Post.objects.get(id=article_id)
    comments = post.comment_set.order_by('-date_posted')
    context = {
        'post':post,
        'comments':comments,
        # 'user':user
        }

    # if request.method == 'GET':
    #     visitors = post.like_set.all()
    #     print(visitors)
    #     temp = Like()
    #     temp.post = post
    #     temp.visitor = request.user.pk
    #     if temp not in visitors:
    #         post.likes += 1
    #         post.save()
    #         v = Like()
    #         v.visitor = request.user.pk
    #         v.post = post
    #         v.save()

    if request.method == 'POST':
        content = request.POST.get('addComment')
        com = Comment(post=post,comment=content)
        com.author = request.user.username
        com.image_url = request.user.profile.image.url
        com.save()
        # return render(request, 'article/full_article1.html', context=context)
        return redirect(f'../../{post.title}/{post.id}')

    return render(request, 'article/full_article1.html', context=context)

@login_required
def addArticle(request):
    newPost = Post()
    user = User.objects.get(id=request.user.pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        newPost.title=title
        newPost.content=content
        newPost.author = user
        newPost.save()

    return render(request , 'article/add_article.html')

@login_required
def editArticle(request,title, article_id):
    # print(article_id)
    post = Post.objects.get(id=article_id)
    if request.user.pk == post.author.pk:
        comments = post.comment_set.all()

        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            # return redirect(fullArticle, user=post.title, article_id=post.id)
            return redirect(f'../../../article/{post.title}/{post.id}')

        context = {
            'post':post,
            'comments':comments,
            }
        return render(request, 'article/edit_article.html', context=context)
    else:
        return HttpResponse('<p> You are not authorised to edit this article </p>') 


def search(request):
    query = request.GET['query']
    if len(query) == 0 or len(query) > 32:
        allposts = Post.objects.none()
    else:
        postTitle = Post.objects.filter(title__icontains=query)
        postContent = Post.objects.filter(content__icontains=query)
        allposts = postTitle.union(postContent)
    # print(allposts)
    context = {
        'allposts':allposts,
        'query':query
    }
    return render(request, 'article/search.html',context)
    # return HttpResponse('This is search')



def viewProfile(request, username):
    user = User.objects.get(username = username)
    context = {
        'user':user
    }
    return render(request, 'article/profilepublic.html',context)