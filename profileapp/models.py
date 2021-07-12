from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # 이 프로필의 주인이 누구인지, OneToOneField=profile과 user객체를 하나씩 연결해준다
    # on_delete = 이 객체가 사라질 때 CASCADE= 이객체도 사라지는 행동, related_name= 유저에 profile에 바로 접근가능하게 이름을 지정 ex)request.user.profile.nickname하면 닉네임을 받을 수 있다
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)  #upload_to= 서버내부에 이미지가 저장될 경로, null을 쓴 이유는 이미지가 없어도 괜찮다는 것
    nickname = models.CharField(max_length=20, unique=True, null=True)  #unique=닉네임은 유일한 닉네임만 가지게
    message = models.CharField(max_length=100, null=True)   #상태메세지

