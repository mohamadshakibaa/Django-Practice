from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from website.forms import NameForm, ContactForm, NewsletterForm

def index(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def elements(request):
    return render(request, 'website/elements.html')

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact')
    else:
        return HttpResponseRedirect('/')
    form = NewsletterForm()
    return render(request, 'website:newsletter', {'form': form})

# def test(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Done')
#         else:
#             return HttpResponse('not valid')
#     form = ContactForm()
#     return render(request, 'test.html', {'form': form})

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})