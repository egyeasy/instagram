from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        # 여기서 form.save()로 끝내줘도 되나, validation을 넣도록 하자.
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
        
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)
    
    
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:list')
    
    
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # 수정내용 DB에 반영
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        # 수정내용 편집 가능한 페이지 보여주기
        form = PostModelForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'posts/update.html', context)