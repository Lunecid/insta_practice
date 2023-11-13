from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required 
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')

    context = {
        'posts': posts,
    }

    return render(request,'index.html',context)


def create(request):
    if request.method == 'POST':
        # 사진은 FILES 요청에 있다
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request,'form.html',context)

@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)


    # 이미 좋아요 버튼을 누른 경우
    # if post in user.like_posts.all():
    if user in post.like_users.all():
        post.like_users.remove(user)
    # 좋아요 버튼을 아직 안누른경우
    else:
        post.like_users.add(user)



    # user.like_posts.add(post) 위와 같은 값의 코드


    return redirect('posts:index')



