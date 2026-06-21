from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag
def count():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='total')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    
    return {'categories': cat_dict} 