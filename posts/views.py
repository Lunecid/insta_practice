from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request,'index.html',context)


def create(request):
    if request.method == 'POST':
        # 사진은 FILES 요청에 있다
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request,'form.html',context)

