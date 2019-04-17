from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # UserCreationForm에 있는 Meta 클래스의 fields를 그대로 쓰겠다
        # fields = UserCreationForm.Meta.fields