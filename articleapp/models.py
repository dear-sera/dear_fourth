from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    # SET_NULL= 회원탈퇴를 했을 때 article은 주인이없는 게시글로 남을 수 있게된다, 이때 null=True를 꼭 붙여 사용해줘야 한다
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

