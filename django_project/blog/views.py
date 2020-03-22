from django.shortcuts import render
# from django.http import HttpResponse
# def about(request): 
#     return HttpResponse("<h1>Tirth's Blog About</h1>")

posts = [
    {
        'author': 'Tirth',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted': 'March 21, 2020'
    },
    {
        'author': 'Rohit',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted': 'March 23, 2099'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts,

    }
    return render(request, 'blog/home.html', context)



def about(request): 
    return render(request, 'blog/about.html',{'title':'About2'})

