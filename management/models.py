from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=20,verbose_name='姓名')
    student_sex = models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='male',verbose_name='性别')
    student_id = models.CharField(max_length=12,verbose_name='学号',primary_key=True)
    password = models.CharField(max_length=20,verbose_name='密码',default='123456789')
    student_building=models.ForeignKey(to='Building',verbose_name='宿舍楼',on_delete=models.CASCADE)
    student_room =models.ForeignKey(to='Room',verbose_name='宿舍房间',on_delete=models.CASCADE)
    def __str__(self):
        return self.student_id
    class Meta:
        verbose_name = '学生'
        verbose_name_plural ='学生'


class Mistake(models.Model):
    mistake_id = models.ForeignKey(to='Student',verbose_name=' 学号',on_delete=models.CASCADE)
    case = models.CharField(max_length=100,verbose_name='违纪原因')
    date = models.DateTimeField('违纪时间')
    class Meta:
        verbose_name='违纪信息'
        verbose_name_plural='违纪信息'



class Room(models.Model):
    room_id = models.CharField(max_length=3,verbose_name='宿舍号')
    room_building =models.ForeignKey(to='Building',verbose_name='宿舍楼',on_delete=models.CASCADE)
    room_water = models.FloatField(verbose_name='水费')
    room_electricity = models.FloatField(verbose_name='电费')

    def __str__(self):
        return self.room_id
    class Meta:
        verbose_name = '宿舍房间'
        verbose_name_plural='宿舍房间'

class Building(models.Model):
    building_name = models.CharField(max_length=10, verbose_name="楼栋",primary_key=True)
    class Meta:
        verbose_name = '宿舍楼'
        verbose_name_plural = '宿舍楼'
    def __str__(self):
        return self.building_name


