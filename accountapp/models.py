from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)  #null=공백에 대해서 없어도 되는지 = 안되니까 false
