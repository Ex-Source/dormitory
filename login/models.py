from django.db import models
from management.models import Student
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10,verbose_name='姓名')
    uid = models.CharField(max_length=20,verbose_name ='账号')
    password = models.CharField(max_length=20,verbose_name='密码')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '学生账号'
        verbose_name_plural = '学生账号'
