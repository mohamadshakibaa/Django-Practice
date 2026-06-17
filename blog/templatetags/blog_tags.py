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