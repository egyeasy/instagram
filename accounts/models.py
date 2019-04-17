from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 여기 User와는 다른 User여야 한다. 
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")