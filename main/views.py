from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def articles(request):
    return render(request, 'main/articles.html')

def creativeWorks(request):
    return render(request, 'main/creativeWorks.html')