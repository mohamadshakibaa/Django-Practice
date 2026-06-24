from django.urls import path
from . import views

app_name = 'website' 

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('elements', views.elements, name='elements'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('test', views.test, name='test'),
]
