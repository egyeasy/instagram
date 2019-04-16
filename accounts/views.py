from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login # 함수명과 겹치지 않도록 설정
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    # 회원가입 시키기
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save의 return을 user로 받아서 로그인에 쓰겠다.
            auth_login(request, user)
            # auth_login(request, form.get_user()) # 이렇게 써도 됨
            return redirect('posts:list')
    # 회원가입 폼 보여주기
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        # 실제 로그인(세션에 유저 정보를 넣는다.)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('posts:list')
    else:
        # 유저로부터 username과 비밀번호를 받는다.
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')