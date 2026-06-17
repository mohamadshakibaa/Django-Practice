from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def count():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='total')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts':posts}