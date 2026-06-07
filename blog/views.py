from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, pk=pid)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    context = {
                'post': post,
                'next_post': next_post,
                'prev_post': prev_post,
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

    context = {
        'post': post
    }

    return render(request, 'test.html', context)