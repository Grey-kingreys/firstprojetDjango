from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/base_blog.html')

# Create your views here.
