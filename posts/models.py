from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # 사진 없는 것도 가능하게 설정
    
    def __str__(self):
        return self.content