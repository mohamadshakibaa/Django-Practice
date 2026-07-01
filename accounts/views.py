from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
def login_view(request):
#     if request.user.is_authenticated:
#         msg = f'user is attenticated {request.user.username}'
#     else:
#         msg = 'user is not attenticated '
#                                                 , {'msg': msg}
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('/')
    
    if request.method == 'POST':
        data = request.POST.copy()
        if '@' in data['username']:
            user = User.objects.filter(email=data['username']).first()
            if user:
                data['username'] = user.username
        form = AuthenticationForm(request=request, data=data)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            if not next_url or next_url == "None":
                next_url = "/"
            return redirect(next_url)
        
    else:               
        form = AuthenticationForm()
    
    context = {'form': form, 'next': request.GET.get('next')}
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)       # this part very important for your signup
                return redirect('/')
            
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')