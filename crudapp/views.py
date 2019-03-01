from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


def index(request):
    return render(request, 'index.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id): 
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def update(request, blog_id):
    updates= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'updates': updates})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.body = request.POST['body']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('CRUD')

# def blogpost(request):
#     # 1.입력된 내용을 처리하는 기능-> POST
#     if request.method == 'POST':
#         form = BlogPost(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.pub_date = timezone.now()
#             post.save()
#         return redirect('home')
#     # 2. 빈 페이지를 띄워주는 기능 -> GET
#     else:
#         form = BlogPost()
#         return render(request, 'new.html', {'form':form})


def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    # return render(request, 'home.html', {'destroy': destroy})
    return redirect('CRUD')