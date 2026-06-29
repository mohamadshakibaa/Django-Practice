from django.shortcuts import render

# Create your views here.
def login_view(request):
#     if request.user.is_authenticated:
#         msg = f'user is attenticated {request.user.username}'
#     else:
#         msg = 'user is not attenticated '
#                                                 , {'msg': msg}
    return render(request, 'accounts/login.html')

def logout_view(request):
    pass

def signup_view(request):
    return render(request, 'accounts/signup.html')