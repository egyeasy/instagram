from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(
        label="content",
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 50,
            'placeholder': '지금 뭘 하고 계신가요?',
    }))
    
    class Meta:
        model = Post
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = ['content', 'image'] # 이미지 추가
        

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']