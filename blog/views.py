from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


def blog_view(request,**kwargs):
    posts = Post.objects.filter(status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts = Paginator(posts, 3)
    try: 
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number) 
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment send to approve')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment dont send to approve')
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, pk=pid)
    if post.login_require and not request.user.is_authenticated:
        login_url = reverse('accounts:login')
        return redirect(f'{login_url}?next={request.path}')

    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    comments = Comment.objects.filter(post=post.id, approved=True)

    form = CommentForm()

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/blog-single.html', context)


# def test(request, pid):
#     posts = get_object_or_404(Post, pk = pid)
#     context = {'posts': posts}
#     date = Post.objects.all()
#     publish = date[0].published_date
#     date_now = datetime.now()
#     if publish == date_now:
#         print(posts.published_date)
#     else:
#         print("NO")
#     return render(request, 'test.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    if post.published_date > timezone.now():
        return render(request, '404.html', status=404)
    
    context = {'post': post}
    return render(request, 'test.html', context)


def test1(request):
    return render (request, 'test.html')

#  (((((tabdil shod be 2url dar 1 view)))))
# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)