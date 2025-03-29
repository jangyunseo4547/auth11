from .models import User
from django.contrib.auth.forms import UserCreationForm


# 로그인 
class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username',)


