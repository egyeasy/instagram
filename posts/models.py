from django.db import models
# from django.auth 써도 되는데 아래는 다른 방법
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # 사진 없는 것도 가능하게 설정
    # User와의 연결고리 필요
    # user = models.ForeignKey(User, ) 이렇게 하지 않고
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user와의 연결고리 2 (M:N) Like
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)