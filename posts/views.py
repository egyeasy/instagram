from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        # 여기서 form.save()로 끝내줘도 되나, validation을 넣도록 하자.
        if form.is_valid():
            form.save()
            return redirect('posts:create')
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)