from django.conf import settings
from turtle import bgcolor
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog, Article
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

#=============================================================================================== errors

def raise_401 (request, text = None): return render(request, 'errors/401.html', {'text': text})
def raise_403 (request, text = None): return render(request, 'errors/403.html', {'text': text})
def raise_404 (request, text = None): return render(request, 'errors/404.html', {'text': text})
def raise_500 (request, text = None): return render(request, 'errors/500.html', {'text': text})

#=============================================================================================== decorators

def check_401 (func):
    def wrap (request, *args, **kwargs):
        if not request.user.is_authenticated: return raise_401 (request)
        return func(request, *args, **kwargs)

    return wrap

def check_403 (check_for):
    def decorator (func):
        if check_for == 'authorship':
            def wrap (request, aid = None):
                if (not Article.objects.get(id = aid).blog.author == request.user.username and
                    not request.user.is_superuser):
                    return raise_403(request, 'Вы не можете редактировать эту статью.')
                return func(request,  aid)

        elif check_for == 'new_authorship':
            def wrap (request):
                aid = request.POST.get('id')
                if (aid != 'new' and
                    not Article.objects.get(id = aid).blog.author == request.user.username and
                    not request.user.is_superuser):
                    return raise_403(request, 'Вы не можете редактировать эту статью.')
                return func(request)

        return wrap
    return decorator

def check_404 (elem):
    def decorator (func):
        if elem == 'blog':
            def wrap (request, blog = None):
                if blog != None and len(Blog.objects.filter(name = blog)) <= 0:
                    return raise_404 (request, 'К сожалению, такого блога не существует.')
                return func(request, blog)

        elif elem == 'article':
            def wrap (request, aid = None):
                if aid != None and len(Article.objects.filter(id = aid)) <= 0:
                    return raise_404 (request, 'К сожалению, такой статьи не существует.')
                return func(request, aid)

        elif elem == 'new_article':
            def wrap (request):
                aid = request.POST.get('id')
                if aid != 'new' and aid != None and len(Article.objects.filter(id = aid)) <= 0:
                    return raise_404 (request, 'К сожалению, такой статьи не существует.')
                return func(request)
            

        return wrap
    return decorator

def check_500 (func):
    if not settings.DEBUG:
        def wrap (request, *args, **kwargs):
            try: return func(request, *args, **kwargs)
            except: return raise_500 (request)
            
        return wrap
    else: return func

#=============================================================================================== requests

@check_404('blog')
@check_500
def index (request, blog = None):
    if blog != None: blog = Blog.objects.get(name = blog)
    user_blogs = ([] if request.user == None else Blog.objects.filter(author = request.user.username))

    content = {
        'blogs': Blog.objects.all(), 
        'articles': Article.objects.order_by('-pub_date'),
        'selected': blog,
        'USER': request.user,

        'user_blogs': user_blogs,
        'can_add_article': (False if len(user_blogs) <= 0 else True)
    }
    return render(request, 'blogs/index.html', content)

@check_500
def registration (request):
    user_names = [user.username for user in User.objects.all()]
    return render(request, 'blogs/registration.html', {'used': user_names})

@check_500
def submit_registration (request):
    user = User.objects.create_user(request.GET['name'], request.GET['email'], request.GET['password'])
    user.groups.add(Group.objects.get(name = 'authors'))
    user.save()
    django_login(request, user)
    return redirect(index)

@check_500
def login (request):
    return render(request, 'blogs/login.html', {'auth_status': True})

@check_500
def no_login (request):
    return render(request, 'blogs/login.html', {'auth_status': False})

@check_500
def submit_login (request):
    global auth_status
    user = authenticate(username = request.GET['name'], password = request.GET['password'])
    if user == None: return redirect(no_login)
    else: 
        django_login(request, user)
        return redirect(index)

@check_500
def logout (request):
    if request.user.is_authenticated: django_logout(request)
    return redirect(index)

@check_401
@check_500
def change_password (request):
    user_names = [user.username for user in User.objects.all()]
    return render(request, 'blogs/change_password.html', {'used': user_names})

@check_401
@check_500
def submit_change (request):
    user = User.objects.get(username = request.GET['name']).first()
    if user != None:
        user.set_password(request.GET['password'])
        user.save()

    return submit_login(request)

@check_401
@check_500
def new_blog (request):
    blog = Blog.objects.create(name = request.GET['name'], author = request.user.username)
    blog.save()
    return redirect(index)

@check_404('article')
@check_500
def article (request, aid = 0):
    content = {
        'article': Article.objects.get(id = aid),
        'USER': request.user,
    }
    return render(request, 'blogs/article.html', content)

@check_401
@check_500
def new_article (request):
    if len(Blog.objects.filter(author = request.user.username)) > 0:
        content = {
            'id': 'new',
            'heading': '',
            'text': '',
            'img': '',
            'sel_blog': '',
            
            'blogs': Blog.objects.all(),
            'USER': request.user,
        }
        return render(request, 'blogs/edit_article.html', content)
    else: return redirect(index)

@check_401
@check_404('article')
@check_403('authorship')
@check_500
def edit_article (request, aid):
    art = Article.objects.get(id = aid)
    content = {
        'id': aid,
        'heading': art.heading,
        'text': art.text,
        'img': (art.img.url if art.img else ''),
        'sel_blog': art.blog.name,
        
        'blogs': Blog.objects.filter(author = request.user.username),
        'USER': request.user,
    }
    return render(request, 'blogs/edit_article.html', content)

@check_401
@check_404('new_article')
@check_403('new_authorship')
@check_500
def submit_article (request):
    if request.POST.get('id') == 'new':
        a = Article.objects.create(heading = request.POST.get('heading'),
                                   text = request.POST.get('text'),
                                   img = request.FILES.get('img'),
                                   blog = Blog.objects.filter(name = request.POST.get('blog')).first())
    
    else:
        a = Article.objects.get(id = int(request.POST.get('id')))
        a.heading = request.POST.get('heading')
        a.text = request.POST.get('text')
        a.img = request.POST.get('img')
        a.blog = Blog.objects.filter(name = request.POST.get('blog')).first()

    a.save()
    return redirect(index)

def get_img (request, img = None):
    return HttpResponse(Article.objects.filter(img = 'media/'+img).first().img)