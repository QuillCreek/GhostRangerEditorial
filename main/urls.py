from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/articles', views.articles, name='articles'),
    path('/creativeWorks', views.creativeWorks, name='creativeWorks'),
]